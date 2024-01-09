from django.db import models
from customer0.models import Client

class Czech(models.Model):
    chec_bearer = models.ForeignKey(Client, null=True, on_delete=models.SET_NULL)
    check_book = models.IntegerField(unique=True)
    sayad = models.CharField(max_length=16, unique=True)
    dueـdate = models.CharField(max_length=15)
    amount = models.CharField(max_length=20)
    national_code = models.CharField(max_length=20, unique=True)
    destination = models.CharField(max_length=100, null=True, blank=True)
    dueـdate = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    holder = models.CharField(max_length=100, null=True, blank=True)

    class RegistereChoice(models.TextChoices):
        Yes = 'yes'
        No = 'no'

    is_registered = models.CharField(max_length=16, choices =RegistereChoice, default=RegistereChoice.No)

    class Meta:
        ordering = ['-check_book', ]


    check_photo = models.ImageField( blank=True, null=True, upload_to="chekha")

    def __str__(self) -> str:
        return str(self.id) +"--"+ str(self.check_book)



class Received(models.Model):
    chek = models.ManyToManyField(Czech, blank=True)
    cash = models.IntegerField(blank=True, null=True)
    date = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    @property
    def total_received(self):
        total_price = sum(int(t.amount) or 0 for t in self.chek.all())
        total_cash = self.cash or 0
        total = total_price + total_cash
        return total or 0


    def __str__(self):
        return  str(self.id) +str('--')+ str(self.total_received)
