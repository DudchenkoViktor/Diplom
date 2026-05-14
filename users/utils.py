import re

from django.core.exceptions import ValidationError


def numeric_validator(value):
    if not value.isdigit():
        raise ValidationError("This field must contain only digits.")
    if int(value) > 99:
        raise ValidationError("The value must not exceed 99.")

def fullname_validator(value):
    pattern = r'^[a-zA-Z]+$'
    if not re.match(pattern, value):
        raise ValidationError("This field must contain only English letters.")