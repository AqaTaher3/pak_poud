from django.db import models
from customer0.models import ZiNaf, Moshtary


class Tage(models.Model):
    jens = models.CharField(max_length=16)
    vazn = models.DecimalField(max_digits=10, decimal_places=2)
    metraj = models.DecimalField(max_digits=10, decimal_places=2)
    class Meta:
        ordering = ['-vazn', ]

    def __str__(self) -> str:
        return self.vazn+self.jens


class FactorForoosh(models.Model):
    kharidar = models.ManyToManyField(Moshtary)
    tage_ha = models.ManyToManyField(Tage)
    fee = models.DecimalField(max_digits=9, decimal_places=0)
    tarikhe_foroosh = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    class Meta:
        ordering = ['-tarikhe_foroosh', ]

    def __str__(self) -> str:
        return self.kharidar[0:50] + self.tarikhe_foroosh