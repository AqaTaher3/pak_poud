from django.contrib import admin

from .models import Chek, Daryafti

admin.site.register(Chek)


class DaryaftiAdmin(admin.ModelAdmin):
    list_display = [ 'nagdi', 'kole_daryafti']
admin.site.register(Daryafti, DaryaftiAdmin)
