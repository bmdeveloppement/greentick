from django import forms
from request.models import Type
from user.models import User


class CreateRequestForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    type = forms.ModelChoiceField(label='Type', queryset=None)
    validators = forms.CharField(label='Validators', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=100000)
    file_1 = forms.FileField(label='Attached file')
    file_2 = forms.FileField(label='Attached file 2')
    file_3 = forms.FileField(label='Attached file 3')
    tracking_reference = forms.CharField(label='Tracking reference', max_length=200)

    def __init__(self, *args, **kwargs):
        super(CreateRequestForm, self).__init__()

        # Get the current user
        user = kwargs.pop('user', None)

        # Fill the 'type' choice
        self.fields['type'] = forms.ModelChoiceField(queryset=Type.get_for_user(user))
