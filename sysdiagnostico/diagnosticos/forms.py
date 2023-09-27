from django import forms
from .models import Diagnosticos


class DiagnosticosForm(forms.ModelForm):
    class Meta:
        model = Diagnosticos
        fields = '__all__'

