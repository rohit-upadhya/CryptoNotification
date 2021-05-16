from django import forms
from django.db import models
from django.forms import fields
from .models import Crypto

class CryptoForm(forms.ModelForm):
    class Meta:
        model = Crypto
        fields = "__all__"