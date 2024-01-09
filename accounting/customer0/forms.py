from django import forms

from django.forms import ModelForm
from .models import Client, Recipient


class CreateClientForm(ModelForm):
    class Meta:
        model = Client
        fields = "__all__"


class CreateRecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = "__all__"
