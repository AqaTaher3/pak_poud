from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from customer0.models import Moshtary





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
    shomare_factor = models.IntegerField(blank=True, null=True)
    kharidar = models.ForeignKey(Moshtary, on_delete=models.SET_NULL, null=True)
    tage = models.ManyToManyField(Tage, blank=True)
    geymat = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=240)
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
    def Mablag_kol(self):
        if self.tage.exists() and self.tage.first().jens_parche in ['nil', 'bangal']:
            total_price = float(self.vazn_kol) * float(self.geymat or 0)
        else:
            total_price = float(self.metraj_kol) * float(self.geymat or 0)
        return total_price

    # @property
    # def sum_total_invoice(self):
    #     total = sum(t.Mablag_kol for t in self.tage.all())
    #     return total
    class Meta:
        ordering = ['-shomare_factor', ]
        verbose_name_plural = "Factors"
    def __str__(self) -> str:
        return str(self.shomare_factor) +"---"+ str(self.kharidar)


@receiver(pre_save, sender=Foroosh)
def calculate_total(sender, instance, created=False , **kwargs):
    if created:
        total = 0
        instance.save()

        for tage in instance.tage.all():
            total += tage.Mablag_kol
        instance.total = total
        instance.save()  # ذخیره تغییرات
