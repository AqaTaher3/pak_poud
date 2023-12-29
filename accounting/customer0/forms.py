from django import forms

from django.forms import ModelForm
from .models import Moshtary


class CreateMoshtaryForm(ModelForm):
    class Meta:
        model = Moshtary
        fields = "__all__"


class UpdateMoshtariForm(forms.Form):
    class Meta:
        model = Moshtary
        fields = "__all__"
