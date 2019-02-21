from channels.routing import route_class
from .consumers import LotteryTracker

channel_routing = [
    route_class(LotteryTracker, path=LotteryTracker.url_pattern, )
]
