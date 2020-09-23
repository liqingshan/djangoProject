import logging
import time

from rest_framework.throttling import BaseThrottle, SimpleRateThrottle

logger = logging.getLogger(__name__)

class TokenBucket(object):

    # rate是令牌发放速度，capacity是桶的大小
    def __init__(self, rate, capacity):
        self._rate = rate
        self._capacity = capacity
        self._current_amount = 0
        self._last_consume_time = int(time.time())

    # token_amount是发送数据需要的令牌数
    def consume(self, token_amount):
        increment = (int(time.time()) - self._last_consume_time) * self._rate  # 计算从上次发送到这次发送，新发放的令牌数量
        print("increment " + str(increment))
        self._current_amount = min(
            increment + self._current_amount, self._capacity)  # 令牌数量不能超过桶的容量
        if token_amount > self._current_amount:  # 如果没有足够的令牌，则不能发送数据
            return False
        self._last_consume_time = int(time.time())
        self._current_amount -= token_amount
        return True

    @property
    def last_consume_time(self):
        return self._last_consume_time


_token_bucket = TokenBucket(1, 100)
logger.info(_token_bucket.last_consume_time)


class TokenBucketRateThrottle(BaseThrottle):

    def allow_request(self, request, view):
        logging.info("allow_request start")
        res = _token_bucket.consume(1)
        if not res:
            logger.info("exceed token bucket")
            return {
                "status": "status",
            }
        return True
