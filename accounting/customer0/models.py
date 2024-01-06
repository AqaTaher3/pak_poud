from django.db import models
# from django.contrib.auth.models import User



choices = [
    ('hagigi' , 'hagigi'),
    ('hogogi' , 'hogogi')
]


class Moshtary(models.Model):
    name = models.CharField(max_length=50)
    kode_meli = models.CharField(max_length=16, blank =True, null = True)
    shomare = models.CharField(max_length=16)
    address = models.TextField()
    sagfe_etebar = models.CharField(max_length=16)

    class Meta:
        ordering = ['name', ]

    def __str__(self) -> str:
        return self.name[0:50]

class ZiNaf(models.Model):
    name = models.CharField(max_length=50)
    hagigi_or_hogogi = models.CharField(max_length=16, choices =choices)
    kode_meli = models.CharField(max_length=11)

    class Meta:
        ordering = ['-name', ]

    def __str__(self) -> str:
        return self.name[0:50]
