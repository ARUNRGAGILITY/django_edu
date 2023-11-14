# custom_filters.py

from django import template
from django.templatetags.static import PrefixNode

register = template.Library()

@register.filter
def replace_static(value):
    # Replace `{% static %}` tags with the actual URL
    return PrefixNode.handle_simple("static", value)
