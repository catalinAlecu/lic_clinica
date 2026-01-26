from django import forms
from .models import Programare


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
