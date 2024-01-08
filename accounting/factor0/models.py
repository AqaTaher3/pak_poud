from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from customer0.models import Moshtary
from chek0.models import Chek


class Tage(models.Model):
    jens_parche = models.CharField(max_length=16, default='nil-bangal')
    rangrazi = models.CharField(max_length=30, default='sooper_derakhshan')
    vazn = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    metraj = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=120)

    class Meta:
        ordering = ['-jens_parche', '-vazn', '-metraj', ]
        verbose_name_plural = "Tage_ha"

    def __str__(self) -> str:
        return str(self.vazn)


class Foroosh(models.Model):
    hesab_daryafti = models.ForeignKey('Hesab_daryafti', on_delete=models.SET_NULL, blank= True, null=True)
    geymat = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=240)
    kharidar = models.ForeignKey(Moshtary, on_delete=models.SET_NULL, null=True)
    shomare_factor = models.IntegerField(blank=True, null=True)
    tage = models.ManyToManyField(Tage, blank=True)
    tarikhe_foroosh = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def vazn_kol(self):
        total_vazn = sum(t.vazn or 0 for t in self.tage.all())
        return total_vazn

    @property
    def metraj_kol(self):
        total_metraj = sum(t.metraj or 0 for t in self.tage.all())
        return total_metraj

    @property
    def mablag_kol(self):
        if self.tage.exists() and self.tage.first().jens_parche in ['nil', 'bangal']:
            total_price = float(self.vazn_kol) * float(self.geymat or 0)
        else:
            total_price = float(self.metraj_kol) * float(self.geymat or 0)
        return total_price

    @property
    def albagi_hesab(self):
        total_daryafti = (self.hesab_daryafti.kole_daryafti or 0)
        albagi = self.mablag_kol - total_daryafti
        return albagi

    @property
    def baste_shod(self):
        if self.albagi_hesab == 0:
            return "baste"
        else:
            return "baz"

    class Meta:
        ordering = ['-shomare_factor', ]
        verbose_name_plural = "Factors"
    def __str__(self) -> str:
        return   str(self.id) +str('--')+ str(self.shomare_factor) +str('--')+   str(self.kharidar)

class Hesab_daryafti(models.Model):
    chek = models.ManyToManyField(Chek, null=True, blank=True)
    nagdi = models.IntegerField(blank=True, null=True)

    tarikhe_daryaft = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def kole_daryafti(self):
        total_price = sum(int(t.mablag) or 0 for t in self.chek.all())
        total_nagdi = self.nagdi
        total = total_price + total_nagdi

        return total

    def __str__(self):
        return  str(self.id) +str('--')+ str(self.kole_daryafti)
