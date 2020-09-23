from django.db import models


# 限流规则(令牌桶)
class ThrottleStrategyModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    rate = models.IntegerField(u"速率")
    capacity = models.IntegerField(u"容量")
    comment = models.CharField(max_length=100)

    class Meta:
        ordering = ('created',)
        db_table = "throttle_strategy"

    def save(self, *args, **kwargs):
        super(ThrottleStrategyModel, self).save(*args, **kwargs)
