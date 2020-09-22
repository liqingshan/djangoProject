from rest_framework.throttling import BaseThrottle, SimpleRateThrottle


class VisitThrottle(SimpleRateThrottle):
    scope = 'anonymous'

    def get_cache_key(self, request, view):
        return self.get_ident(request)


class UserThrottle(SimpleRateThrottle):
    scope = 'user'

    def get_cache_key(self, request, view):
        return request.user.username
