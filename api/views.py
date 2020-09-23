from django.contrib.auth.models import User
from django.http import HttpResponse
from rest_framework import viewsets

from api.serializers import UserSerializer


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


def test(request):
    data = "this is a test"

    print(request.user.username)

    print(data)
    return HttpResponse(data, content_type='application/json')
