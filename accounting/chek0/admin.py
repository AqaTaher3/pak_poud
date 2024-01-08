from django.contrib import admin

from .models import Chek, Hesab_daryafti

admin.site.register(Chek)


class Hesab_daryaftiAdmin(admin.ModelAdmin):
    list_display = [ 'nagdi', 'kole_daryafti']
admin.site.register(Hesab_daryafti, Hesab_daryaftiAdmin)
