from django.db import models
# from django.contrib.auth.models import User





class Client(models.Model):
    name = models.CharField(max_length=50)
    national_code = models.CharField(max_length=16, blank =True, null = True)
    phonr_number = models.CharField(max_length=16)
    address = models.TextField()
    creditـlimit = models.CharField(max_length=16)

    class Meta:
        ordering = ['name', ]
        verbose_name_plural = "Moshtari_ha"

    def __str__(self) -> str:
        return self.name[0:50]
    @property
    def full_name(self):
        "Returns the person's full name."
        return f"{self.name} {self.last_name}"

class Transferee(models.Model):
    name = models.CharField(max_length=50)

    class Nationa_code_type(models.TextChoices):
        Hagigi = 'hagigi'
        Hogogi = 'hogogi'

    real_or_lega_nationality = models.CharField(max_length=16, choices =Nationa_code_type)
    national_code = models.CharField(max_length=16, blank =True, null = True)

    class Meta:
        ordering = ['-name', ]
        verbose_name_plural = "Zinaf_ha"

    def __str__(self) -> str:
        return self.name[0:50]
