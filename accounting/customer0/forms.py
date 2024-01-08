from django import forms

from django.forms import ModelForm
from .models import Client


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"
