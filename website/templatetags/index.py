from django import template
from website.models import *

register = template.Library()


@register.filter
def index(indexable, i):
    return indexable[i]
