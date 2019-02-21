from django import template
from django.template import TemplateSyntaxError, Context

register = template.Library()


# two following random strings are needed to prevent usage of tracking_time and tracking_focus twice
# see more here: https://stackoverflow.com/questions/51786795/check-that-tag-is-used-in-template-only-once/


@register.inclusion_tag('lot/tags/LotteryTracker.html', takes_context=True, name='lottery_listener')
def tracking_lotteries(context, *args, **kwargs):
    return context
