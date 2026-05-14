from django import template
from django.utils.http import urlencode

dict_sort = {
    '-last_name': 'Z-A',
    'last_name': 'A-Z',
    'experience': 'By experience',
    'age': 'By age'
}

register = template.Library()

@register.filter(name='sort_name')
def sort_name(value):
    return dict_sort.get(value, value)

@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)


