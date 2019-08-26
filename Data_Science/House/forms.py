from django import forms
from django.contrib.auth import authenticate
from .models import Home


class HomeForm(forms.ModelForm):

    class Meta:
        model = Home
        exclude = ['price']
