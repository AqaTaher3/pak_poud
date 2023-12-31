from django import forms

from django.forms import ModelForm
from .models import Chek


class CreateChekForm(ModelForm):
    class Meta:
        model = Chek
        fields = "__all__"
