import ipaddress

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
    allow_networks = [
        ipaddress.ip_network('10.53.0.0/20'),
        ipaddress.ip_network('127.0.0.1')
    ]

    allow_addresses = []

    @classmethod
    def get_allow_addresses(cls):
        if len(cls.allow_addresses) > 0:
            return cls.allow_addresses

        for network in cls.allow_networks:
            for ip in network:
                cls.allow_addresses.append(ip)

        return cls.allow_addresses

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        ip_addr = ipaddress.ip_address(request.META.get('REMOTE_ADDR'))

        # print('ip addr ' + str(ip_addr))
        # print(self.get_allow_addresses())

        if ip_addr not in self.get_allow_addresses():
            return HttpResponseForbidden()

        return response

