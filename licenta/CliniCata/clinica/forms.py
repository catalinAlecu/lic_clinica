from django import forms
from .models import Programare
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class ProgramareForm(forms.ModelForm):
    class Meta:
        model = Programare
        fields = ['nume_complet', 'telefon', 'specializare', 'data_programare', 'mesaj']
        
        widgets = {
            'data_programare': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'nume_complet': forms.TextInput(attrs={'class': 'form-control'}),
            'telefon': forms.TextInput(attrs={'class': 'form-control'}),
            'specializare': forms.Select(attrs={'class': 'form-control'}),
            'mesaj': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))
    email_confirmation = forms.EmailField(required=True, label="Confirm Email", widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].help_text = None

    class Meta:
        model = User
        fields = ('username', 'email')

    field_order = [
        'username',  
        'password1', 
        'password2',
        'email', 
        'email_confirmation'
    ]

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        email_confirmation = cleaned_data.get("email_confirmation")

        if email and email_confirmation and email != email_confirmation:
            self.add_error('email_confirmation', "Emails do not match.")

        if email and User.objects.filter(email=email).exists():
            self.add_error('email', "Email is already in use.")
       