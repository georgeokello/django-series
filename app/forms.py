from django import forms
from django.forms import fields
from django.forms.models import ModelForm
from . models import Data


class OurForm(ModelForm):
    class Meta:
        model = Data
        fields = ['username','age']