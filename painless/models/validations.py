import re
import string
from django import forms



def validate_phone_number(value):
    pattern = r'^(09)[1-3][0-9]\d{7}$'
    if not re.match(pattern, value):
        raise forms.ValidationError('شماره صحیح وارد نشده است.')

    if not len(value) == 11:
        raise forms.ValidationError('شماره صحیح وارد نشده است')
