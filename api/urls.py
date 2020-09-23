from django.conf.urls import include, url

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'strategy/throttle', views.ThrottleStrategyViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]