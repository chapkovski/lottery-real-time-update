from django import template
from django.conf import settings

register = template.Library()


def valute(value):
    currency = settings.POINTS_CUSTOM_NAME
    return '{:,} {}'.format(value, currency)


@register.filter(name='perc')
def perc(value, arg):
    return valute(int(value * (1 + arg)))


@register.filter(name='p')
def strperc(value):
    return str('{}%'.format('{:,}'.format(int(value * 100))))


@register.inclusion_tag('claire/tags/comprehension_example.html', takes_context=True)
def comprehension_info(context, investment, size):
    context.update({'investment_info': investment.get_comprehension_info(size),
                    'size': size})
    return context
