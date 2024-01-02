from django.db import models
from customer0.models import Moshtary
# Create your models here.

class Chek(models.Model):
    tahvil_dahande = models.ForeignKey(Moshtary, null=True, on_delete=models.SET_NULL)
    daftar = models.IntegerField()
    shomare_sayad = models.CharField(max_length=16)
    tarikh = models.CharField(max_length=15)
    mablag = models.CharField(max_length=20)
    kode_meli = models.CharField(max_length=20)
    magsad = models.CharField(max_length=100, null=True, blank=True)
    tarikhe_daryaft = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    ki_daryaft_kard = models.CharField(max_length=100, null=True, blank=True)
    # ax = models.ImageField()

    class Meta:
        ordering = ['-shomare_sayad', ]

    def __str__(self) -> str:
        return self.daftar
