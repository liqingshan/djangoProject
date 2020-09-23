from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import ThrottleStrategyModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')


#
class ThrottleStrategySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ThrottleStrategyModel
        fields = ('rate', 'capacity', 'comment')
