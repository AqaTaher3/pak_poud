from django.db import models
from customer0.models import Client

class Czech(models.Model):
    chec_bearer = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    check_book = models.IntegerField()
    sayad = models.CharField(max_length=16)
    dueـdate = models.CharField(max_length=15)
    amount = models.CharField(max_length=20)
    national_code = models.CharField(max_length=20)
    destination = models.CharField(max_length=100, null=True, blank=True)
    dueـdate = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    holder = models.CharField(max_length=100, null=True, blank=True)
    check_photo = models.ImageField( blank=True, null=True, upload_to="chekha")

    class Meta:
        ordering = ['-check_book', ]

    def __str__(self) -> str:
        return str(self.check_book)



class Received(models.Model):
    chek = models.ManyToManyField(Czech, blank=True)
    cash = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def tota_received(self):
        total_price = sum(int(t.amount) or 0 for t in self.chek.all())
        total_cash = self.cash or 0
        total = total_price + total_cash
        return total or 0


    def __str__(self):
        return  str(self.id) +str('--')+ str(self.tota_received)
