from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

from api.models import TokenBucketModel, IPAccessControlModel
from api.serializers import UserSerializer, ThrottleStrategySerializer, IPAccessControlSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ThrottleStrategyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = TokenBucketModel.objects.all()
    serializer_class = ThrottleStrategySerializer

    def create(self, request):
        type = request.data.get('', None)
        network = request.data.get('network', None)
        IPAccessControlModel.objects.create(type=type, network=network)
        # print(request.REQUEST.get('type'))
        # super().save(*args, **kwargs)
        # return HttpResponse("OK")
        return Response({'received data': request.data})


class IPAccessControlViewSet(viewsets.ViewSet):
    queryset = IPAccessControlModel.objects.all()
    serializer_class = IPAccessControlSerializer

    parser_classes = (JSONParser,)

    def list(self, request):
        print(request.META)
        queryset = IPAccessControlModel.objects.all()
        serializer = IPAccessControlSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        type = request.data.get('type', None)
        network = request.data.get('network', None)
        IPAccessControlModel.objects.create(type=type, network=network)
        # print(request.REQUEST.get('type'))
        # super().save(*args, **kwargs)
        # return HttpResponse("OK")
        return Response({'received data': request.data})

    def save(self, request):
        # print(request)
        pass

    def getResultCode(data, status=1, msg="成功", msg_level=1):
        """返回 结果 json 要求的字典"""
        '''data 是 list 
        返回参数status 默认1，#0-失败，1-成功，2-部分成功
        msg 默认 成功
        msg_level 默认为1，# 信息展示级别：1-成功，2-询问，3-警告，4-错误
        '''
        return {
            "status": status,
            "msg": msg,
            "data": data,
            "msg_level": msg_level
        }


class GatewayView(APIView):

    @api_view(['GET', 'POST'])
    def get(self, request):
        """
        Return a list of all users.
        """
        # TODO: 转发
        pass