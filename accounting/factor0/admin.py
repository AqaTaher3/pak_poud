from django.contrib import admin

from .models import Tage, Hesab_daryafti, Foroosh


admin.site.register(Tage)
admin.site.register(Hesab_daryafti)


class ForooshAdmin(admin.ModelAdmin):
    list_display = ['shomare_factor', 'kharidar', 'geymat']


admin.site.register(Foroosh, ForooshAdmin)



# , 'Hesab_daryafti','vazn_kol', 'metraj_kol','Mablag_kol', 'albagi_hesab', 'baste_shod'
