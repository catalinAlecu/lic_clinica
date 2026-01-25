from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    email_confirmation = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'email_confirmation')


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for field_name in self.fields:
            self.fields[field_name].help_text = None

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        email_confirmation = cleaned_data.get("email_confirmation")

        if email and email_confirmation and email != email_confirmation:
            self.add_error('email_confirmation', "Emails do not match.")

        return cleaned_data