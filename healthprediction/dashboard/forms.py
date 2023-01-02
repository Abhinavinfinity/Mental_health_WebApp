from django import forms
from .models import Data

class DataForm(forms.ModelForm):
    class Meta:
        model=Data
        fields=['name','country','state','tech_company','student','physical_health','age','sex','family_history']