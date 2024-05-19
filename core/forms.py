from django import forms
from core import models


class AuthorizationForm(forms.Form):
    login = forms.CharField(max_length=150)
    password = forms.CharField(max_length=150)

    def redirection(self, url):
        print(url)
