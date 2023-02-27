from django.template import Library
from django.urls import reverse 
register = Library()

@register.simple_tag
def is_active(request, url):
    # Main idea is to check if the url and the current path is a match
    if reverse(url) == request.path:
        return "is-active"
    return ""