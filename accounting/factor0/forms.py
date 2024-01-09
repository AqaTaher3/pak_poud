from django import forms

from django.forms import ModelForm
from .models import Invoice



class InvoiceForm(ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        # fields = ['id', 'phonr_number factor', 'client', 'amount', 'selling_date', 'updated', ]

#     @property
#     def total_meter(self):
#         total_meter = sum(t.meter or 0 for t in self.tage.all())
#         return total_meter

#     @property
#     def total_meter(self):
#         total_meter = sum(t.meter or 0 for t in self.tage.all())
#         return total_meter

#     @property
#     def total_price(self):
#         if self.tage.exists() and self.tage.first().material in ['nil', 'bangal']:
#             total_price = float(self.total_meter) * float(self.amount or 0)
#         else:
#             total_price = float(self.total_meter) * float(self.amount or 0)
#         return total_price

#     @property
#     def notـreceived(self):
#         total_received = (self.received.tota_received or 0)
#         remaining = self.total_price - total_received
#         return remaining

#     @property
#     def  is_open(self):
#         if self.notـreceived == 0:
#             return "baste"
#         else:
#             return "baz"

#     class Meta:
#         ordering = ['-invoice_number', ]
#         verbose_name_plural = "Factors"
#     def __str__(self) -> str:
#         return   str(self.id) +str('--')+ str(self.invoice_number) +str('--')+   str(self.client)
