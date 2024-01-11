from django import forms

from django.forms import ModelForm
from .models import Invoice, Roll



class CreateInvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'

class CreateRollForm(ModelForm):
    class Meta:
        model = Roll
        fields = '__all__'
