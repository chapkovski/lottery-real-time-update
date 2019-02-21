"""
Just a wrapper tag so lottery info can be included anywhere.
"""
from django import template

register = template.Library()


@register.inclusion_tag('lot/tags/LotteryTracker.html', takes_context=True, name='lottery_listener')
def tracking_lotteries(context, *args, **kwargs):
    return context
