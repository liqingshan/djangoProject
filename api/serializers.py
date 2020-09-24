from django.contrib.auth.models import User
from rest_framework import serializers

from api.models import TokenBucketModel, IPAccessControlModel


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'id', 'username')


#
class ThrottleStrategySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TokenBucketModel
        fields = ('rate', 'capacity', 'comment')


class IPAccessControlSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = IPAccessControlModel
        fields = ('created', 'type', 'network')