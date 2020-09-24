import ipaddress
import logging
import time

from api.models import IPAccessControlModel

logger_stat = logging.getLogger("statistics")
logger = logging.getLogger(__name__)

from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


def get_x_forward_for_addr(request):
    '''获取请求者的IP信息'''
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # 判断是否使用代理
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]  # 使用代理获取真实的ip
    else:
        ip = request.META.get('REMOTE_ADDR')  # 未使用代理获取IP
    print("x_forward_for " + ip)


class AdminSecureMiddleware(object):

    allow_addresses = []

    @classmethod
    def get_allow_addresses(cls):
        if len(cls.allow_addresses) > 0:
            return cls.allow_addresses

        model_list = IPAccessControlModel.objects.filter(type=1)
        for m in model_list:
            ip_net = ipaddress.ip_network(m.network)
            for ip in ip_net:
                cls.allow_addresses.append(ip)

        print(cls.allow_addresses)
        logging.info(cls.allow_addresses)
        logger.info(cls.allow_addresses)

        return cls.allow_addresses

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        ip_addr = ipaddress.ip_address(request.META.get('REMOTE_ADDR'))

        if ip_addr not in self.get_allow_addresses():
            return HttpResponseForbidden()

        response = self.get_response(request)

        return response


class StatisticsMiddleware:
    # 初始化
    def __init__(self, get_response):
        self.get_response = get_response

    # 统计请求时间
    # __call__ 实例对象也将成为一个可调用对象
    def __call__(self, request):
        tick = time.time()
        response = self.get_response(request)
        # 路径
        path = request.path
        # 完整路径
        full_path = request.get_full_path()
        tock = time.time()
        cost = tock - tick
        content_list = []
        content_list.append("now=[%d]" % tock)
        content_list.append("path=[%s]" % path)
        content_list.append("full_path=[%s]" % full_path)
        # 浮点数 保留小数点后6位
        content_list.append("cost=[%.6f]" % cost)
        # 变成字符串
        content = "|@|".join(content_list)
        # 保存在日志文件
        logger_stat.info(content)
        return response
