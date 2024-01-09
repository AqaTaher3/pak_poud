from django.db import models
from customer0.models import Client
from chek0.models import Czech, Received

class Roll(models.Model):
    material = models.CharField(max_length=16, default='nil-bangal')
    dyeing = models.CharField(max_length=30, default='sooper_derakhshan')
    weight = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null=True)
    meter = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=120)
    used_in_invoice = models.BooleanField(default=False, null=True)

    class Meta:
        ordering = ['-material', '-weight', '-meter', ]
        verbose_name_plural = "Rolls"

    def __str__(self) -> str:
        return str(self.weight)

class Invoice(models.Model):
    invoice_number = models.IntegerField(blank=True, null=True, default=2000, unique=True)
    client = models.ForeignKey(Client, on_delete=models.SET_NULL, null=True)
    amount = models.DecimalField(max_digits=6, decimal_places=3, null=True, default=240)
    roll = models.ManyToManyField(Roll)
    received = models.ForeignKey(Received, on_delete=models.SET_NULL, blank=True, null=True)
    selling_date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def total_weight(self):
        return sum(roll.weight for roll in self.roll.all()) if self.roll.exists() else 0

    @property
    def total_meter(self):
        return sum(roll.meter for roll in self.roll.all()) if self.roll.exists() else 0

    @property
    def total_price(self):
        if self.roll.exists():
            if self.roll.filter(material__in=['nil', 'bangal']).exists():
                total_pricee = sum(roll.weight * (self.amount or 0) for roll in self.roll.all())
            else:
                total_pricee = sum(roll.meter * (self.amount or 0) for roll in self.roll.all())
        else:
            total_pricee = 0
        return total_pricee

    @property
    def not_received(self):
        total_received = self.received.total_received if self.received else 0
        remaining = self.total_price - total_received
        return remaining or 0

    @property
    def is_open(self):
        if self.not_received == 0:
            return "baste"
        else:
            return "baz"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.roll.update(used_in_invoice=True)

    class Meta:
        ordering = ['-invoice_number', ]
        verbose_name_plural = "Invoices"

    def __str__(self) -> str:
        return str(self.id) + '--' + str(self.invoice_number) + '--' + str(self.client)
