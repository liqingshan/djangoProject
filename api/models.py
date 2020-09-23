from django.db import models


# 限流规则(令牌桶)
class ThrottleStrategyModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(u"速率")
    capacity = models.IntegerField(u"容量")
    # 1-常规限流 2-
    type = models.IntegerField(u"类型", default=0)
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)
        db_table = "throttle_strategy"

    def save(self, *args, **kwargs):
        super(ThrottleStrategyModel, self).save(*args, **kwargs)

# 转发规则
# class RouteStrategyModel(models.Model):
#     created = models.DateTimeField(auto_now_add=True)