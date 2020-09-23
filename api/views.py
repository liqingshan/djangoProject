from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets

from api.models import ThrottleStrategyModel
from api.serializers import UserSerializer, ThrottleStrategySerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ThrottleStrategyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = ThrottleStrategyModel.objects.all()
    serializer_class = ThrottleStrategySerializer
