from django.db import models
from customer0.models import Client
from chek0.models import Czech, Received

class Roll(models.Model):
    material = models.CharField(max_length=16, default='nil-bangal')
    dyeing = models.CharField(max_length=30, default='sooper_derakhshan')
    weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    meter = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=120)

    class Meta:
        ordering = ['-material', '-weight', '-meter', ]
        verbose_name_plural = "Rolls"

    def __str__(self) -> str:
        return str(self.weight)

class Invoice(models.Model):
    factor_number = models.IntegerField(blank=True, null=True, default=2000)
    kharidar = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    geymat = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=240)
    roll = models.ForeignKey(Roll, on_delete=models.SET_NULL, null=True)

    daryafti = models.ForeignKey(Received, on_delete=models.SET_NULL, blank=True, null=True)

    selling_date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def total_weight(self):
        return self.roll.weight if self.roll else 0

    @property
    def total_meter(self):
        return self.roll.meter if self.roll else 0

    @property
    def total_price(self):
        if self.roll and self.roll.material in ['nil', 'bangal']:
            total_pricee = float(self.total_weight) * float(self.geymat or 0)
        else:
            total_pricee = float(self.total_meter) * float(self.geymat or 0)
        return total_pricee

    @property
    def notـreceived(self):
        total_received = self.daryafti.tota_received if self.daryafti else 0
        remaining = self.total_price - total_received
        return remaining or 0

    @property
    def  is_open(self):
        if self.notـreceived == 0:
            return "baste"
        else:
            return "baz"

    class Meta:
        ordering = ['-factor_number', ]
        verbose_name_plural = "Invoices"

    def __str__(self) -> str:
        return str(self.id) + '--' + str(self.factor_number) + '--' + str(self.kharidar)
