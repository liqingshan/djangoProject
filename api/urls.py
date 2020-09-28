from django.conf.urls import include, url

from api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'strategy/throttle', views.ThrottleStrategyViewSet)
router.register(r'access/ip', views.IPAccessControlViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^gateway', views.GatewayView.as_view()),
    url(r'^gateway2', views.GatewayView2.as_view())
]