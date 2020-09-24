from django.db import models


# 限流规则(令牌桶)
class ThrottleLeakBucketModel(models.Model):
    pass


# 限流规则(令牌桶)
class TokenBucketModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(u"速率")
    capacity = models.IntegerField(u"容量")
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)
        db_table = "throttle_token_bucket"

    def save(self, *args, **kwargs):
        super(TokenBucketModel, self).save(*args, **kwargs)


# IP访问控制
class IPAccessControlModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    # 1-白名单，2-黑名单
    type = models.IntegerField(u"类型", default=0)
    network = models.CharField(u"名单", max_length=20, default='')

    class Meta:
        db_table = "ip_access_control"

    def save(self, *args, **kwargs):
        super(IPAccessControlModel, self).save(*args, **kwargs)
# 转发规则
# class RouteStrategyModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)
