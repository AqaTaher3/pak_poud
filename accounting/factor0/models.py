from django.db import models
from customer0.models import ZiNaf, Moshtary


# related_name='followers'


class Tage(models.Model):
    jens_parche = models.CharField(max_length=16, default='nil-bangal')
    rangrazi = models.CharField(max_length=30, default='sooper_derakhshan')
    vazn = models.IntegerField(blank=True)
    metraj = models.IntegerField(blank=True, default='120')
    geymat = models.IntegerField(null=True, blank=True)
    class Meta:
        ordering = ['-jens_parche', '-vazn', '-metraj', ]

    def __str__(self) -> str:
        return self.vazn


class FactorForoosh(models.Model):
    shomare_factor = models.IntegerField(blank=True, null=True)
    kharidar = models.ForeignKey(Moshtary, on_delete=models.SET_NULL, blank=True, null=True)
    tage = models.ManyToManyField(Tage, null=True, blank=True)
    tarikhe_foroosh = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    Jame_kol = models.IntegerField(null=True, blank=True)

    # def jame_factor(self, tage):
    #     if tage.jens_parche == 'nil' or 'bangal':
    #         total = sum(tage.vazn for tage in self.tage.all())
    #     else:
    #         total = sum(tage.metraj for tage in self.tage.all())
    #     return total * tage.geymat

    # def save(self, *args, **kwargs):
    #     self.Jame_kol = self.jame_factor() 
    #     super().save(*args, **kwargs)

    class Meta:
        ordering = ['-shomare_factor', ]

    def __str__(self) -> str:
        return self.shomare_factor