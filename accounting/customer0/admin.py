from django.contrib import admin

from .models import Client, Recipient

admin.site.register(Client)
admin.site.register(Recipient)
