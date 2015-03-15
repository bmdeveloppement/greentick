from django import forms
from request.models import File, Type


class CreateRequestForm(forms.Form):
    name = forms.CharField(label='Name', max_length=200)
    type = forms.ModelChoiceField(label='Type', queryset=None)
    validators = forms.CharField(label='Validators', max_length=200)
    description = forms.CharField(label='Description', widget=forms.Textarea, max_length=10000)
    tracking_reference = forms.CharField(label='Tracking reference', max_length=200, required=False)

    def __init__(self, *args, **kwargs):
        # Get the current user
        user = kwargs.pop('user', None)

        super(CreateRequestForm, self).__init__(*args, **kwargs)

        # Fill the 'type' choice
        self.fields['type'] = forms.ModelChoiceField(queryset=Type.get_for_user(user))


class UploadFileForm(forms.ModelForm):

    class Meta:
        model = File
        fields = []