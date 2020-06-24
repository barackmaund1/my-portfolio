from django import forms
from .models import Person

class PersonForm(forms.ModelForm):
    class Meta:
        models=Person
        fields=('name','email','subject','message')
