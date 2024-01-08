from django import forms

from django.forms import ModelForm
from .models import Czech


class CreateCzechForm(ModelForm):
    class Meta:
        model = Czech
        fields = "__all__"
