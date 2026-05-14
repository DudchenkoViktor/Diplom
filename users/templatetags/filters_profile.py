from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name='default_no_info')
def default_no_info(value):
    try:
        if value is None or value == "":
            return mark_safe("<i>Information not provided</i>")

        int_value = int(value)

        if int_value < 100:
            return f"{int_value} years"

        return value
    except (ValueError, TypeError):

        return value



