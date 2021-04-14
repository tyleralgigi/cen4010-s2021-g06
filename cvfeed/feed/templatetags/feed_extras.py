import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()


@stringfilter
@register.filter
def create_tag_links(text):
    matches = re.findall(r'(#[a-zA-Z0-9]+\b)', text)
    for m in matches:
        text = text.replace(m, '<a href="/tag/{0}/">{1}</a>'.format(m[1:], m))
    return mark_safe(text)
