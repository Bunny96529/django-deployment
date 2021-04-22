from django import forms
from django.core import validators

def check_for_z(value):
    if value[0].lower()!='z':
        raise forms.ValidationError("does not start with z")



class FormName(forms.Form):
    name=forms.CharField(validators=[check_for_z])
    email=forms.CharField()
    text=forms.CharField(widget=forms.Textarea)
