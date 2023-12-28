from django.db import models
# from django.contrib.auth.models import User


class Moshtary(models.Model):
    name = models.CharField(max_length=16)
    shomare = models.CharField(max_length=16)
    address = models.TextField()
    sagfe_etebar = models.CharField(max_length=16)

    class Meta:
        ordering = ['-name', ]

    def __str__(self) -> str:
        return self.name[0:50]
