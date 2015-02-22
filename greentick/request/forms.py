from django import forms
from request.models import Type


class CreateRequestForm(forms.Form):
    type = forms.ModelChoiceField(label='Type', queryset=None)
    name = forms.CharField(label='Name', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=100000)
    tracking_reference = forms.CharField(label='Tracking reference', max_length=200)

    def __init__(self, *args, **kwargs):
        super(CreateRequestForm, self).__init__()
        user = kwargs.pop('user', None)
        self.fields['type'] = forms.ModelChoiceField(queryset=Type.get_for_user(user))
