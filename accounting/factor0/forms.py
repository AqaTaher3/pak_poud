from django import forms

from django.forms import ModelForm
from .models import Foroosh



class ForooshForm(ModelForm):
    class Meta:
        model = Foroosh
        fields = "__all__"
