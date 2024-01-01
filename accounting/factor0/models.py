from django.db import models
from customer0.models import ZiNaf, Moshtary


class Tage(models.Model):
    jens_parche = models.CharField(max_length=16, default='nil')
    vazn = models.IntegerField()
    metraj = models.IntegerField(default='120')
    class Meta:
        ordering = ['-vazn', ]

    def __str__(self) -> str:
        return self.vazn


class FactorForoosh(models.Model):
    shomare_factor = models.IntegerField(null=True, blank=True)
    kharidar = models.ManyToManyField(Moshtary)
    tage_ha = models.ManyToManyField(Tage)
    fee = models.IntegerField()
    tarikhe_foroosh = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    Jame_kol = models.IntegerField(null=True, blank=True)  # اضافه کردن فیلد Jame_kol

    def jame_factor(self):
        total = sum(tage.vazn for tage in self.tage_ha.all())
        return total * self.fee

    def save(self, *args, **kwargs):
        self.Jame_kol = self.jame_factor()  # محاسبه و ذخیره‌ی مقدار jame_factor در فیلد Jame_kol
        super().save(*args, **kwargs)

    class Meta:
        ordering = ['-tarikhe_foroosh', ]

    def __str__(self) -> str:
        return self.shomare_factor