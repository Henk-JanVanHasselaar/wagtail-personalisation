from django.template import Library
from django.utils import timezone

register = Library()

@register.filter(name='days_since')
def active_days(value, arg):
    """Returns the number of days the segment has been active"""
    if arg == 'enabled':
        delta = timezone.now() - value
        return delta.days
    return 0