from django import forms
from .models import *
class MesurmentForm(forms.ModelForm):
    class Meta:
        model = Mesurment
        fields = ['destination']
