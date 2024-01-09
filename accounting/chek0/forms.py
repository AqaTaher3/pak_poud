from django import forms

from django.forms import ModelForm
from .models import Czech, Received


class CreateCzechForm(ModelForm):
    class Meta:
        model = Czech
        fields = "__all__"


class CreateReceivedForm(ModelForm):
    class Meta:
        model = Received
        fields = "__all__"
