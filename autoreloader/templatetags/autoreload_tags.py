from django import template
from django.utils.safestring import mark_safe
from autoreloader.conf import EXCLUDE


register = template.Library()


@register.simple_tag
def noreload():
    return mark_safe(str(EXCLUDE))
