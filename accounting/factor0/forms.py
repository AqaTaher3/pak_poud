from django import forms

from django.forms import ModelForm
from .models import FactorForoosh


class CreateFactorForooshForm(ModelForm):
    class Meta:
        model = FactorForoosh
        fields = "__all__"
