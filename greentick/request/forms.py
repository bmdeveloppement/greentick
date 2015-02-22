from django import forms
from request.models import Type


class CreateRequestForm(forms.Form):
    type = forms.ModelChoiceField(queryset=None)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        self.fields['type'] = forms.ModelChoiceField(queryset=Type.get_for_user(user))
