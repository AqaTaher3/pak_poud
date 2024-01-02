from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from customer0.models import Moshtary

class Tage(models.Model):
    jens_parche = models.CharField(max_length=16, default='nil-bangal')
    rangrazi = models.CharField(max_length=30, default='sooper_derakhshan')
    vazn = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    metraj = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=120)
    geymat = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=240)

    @property
    def Mablag_kol(self):
        if self.jens_parche in ['nil', 'bangal']:
            total = self.vazn * self.geymat
        else:
            total = self.metraj * self.geymat
        return total

    class Meta:
        ordering = ['-jens_parche', '-vazn', '-metraj', ]

    def __str__(self) -> str:
        return str(self.vazn)


class Foroosh(models.Model):
    shomare_factor = models.IntegerField(blank=True, null=True)
    kharidar = models.ForeignKey(Moshtary, on_delete=models.SET_NULL, blank=True, null=True)
    tage = models.ManyToManyField(Tage, null=True, blank=True)
    tarikhe_foroosh = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, default=240)

    def get_total(self):
        return self.tage.Mablag_kol

    class Meta:
        ordering = ['-shomare_factor', ]


@receiver(pre_save, sender=Foroosh)
def calculate_total(sender, instance, created=False , **kwargs):
    if created:
        total = 0
        instance.save()

        for tage in instance.tage.all():
            total += tage.Mablag_kol
        instance.total = total
        instance.save()  # ذخیره تغییرات