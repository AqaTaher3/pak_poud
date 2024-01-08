from django import forms

from django.forms import ModelForm
from .models import Foroosh



class ForooshForm(ModelForm):
    class Meta:
        model = Foroosh
        fields = '__all__'
        # fields = ['id', 'shomare factor', 'kharidar', 'geymat', 'tarikhe_foroosh', 'updated', ]

#     @property
#     def vazn_kol(self):
#         total_vazn = sum(t.vazn or 0 for t in self.tage.all())
#         return total_vazn

#     @property
#     def metraj_kol(self):
#         total_metraj = sum(t.metraj or 0 for t in self.tage.all())
#         return total_metraj

#     @property
#     def mablag_kol(self):
#         if self.tage.exists() and self.tage.first().jens_parche in ['nil', 'bangal']:
#             total_price = float(self.vazn_kol) * float(self.geymat or 0)
#         else:
#             total_price = float(self.metraj_kol) * float(self.geymat or 0)
#         return total_price

#     @property
#     def albagi_hesab(self):
#         total_daryafti = (self.daryafti.kole_daryafti or 0)
#         albagi = self.mablag_kol - total_daryafti
#         return albagi

#     @property
#     def baste_shod(self):
#         if self.albagi_hesab == 0:
#             return "baste"
#         else:
#             return "baz"

#     class Meta:
#         ordering = ['-shomare_factor', ]
#         verbose_name_plural = "Factors"
#     def __str__(self) -> str:
#         return   str(self.id) +str('--')+ str(self.shomare_factor) +str('--')+   str(self.kharidar)
