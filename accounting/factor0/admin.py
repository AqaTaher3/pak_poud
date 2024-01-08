from django.contrib import admin

from .models import Tage, Hesab_daryafti, Foroosh


admin.site.register(Tage)



# @admin.register(Foroosh)
class ForooshAdmin(admin.ModelAdmin):
    list_display = ['shomare_factor', 'kharidar', 'geymat']
    search_fields = ('shomare_factor', )
    list_filter = ('shomare_factor',)
    prepopulated_fields = {'id':('shomare_factor',)}
    # raw_id_fields = ('id',)


class Hesab_daryaftiAdmin(admin.ModelAdmin):
    list_display = [ 'nagdi', 'kole_daryafti']



admin.site.register(Foroosh, ForooshAdmin)
admin.site.register(Hesab_daryafti, Hesab_daryaftiAdmin)


# , 'hesab_daryafti','vazn_kol', 'metraj_kol','mablag_kol', 'albagi_hesab', 'baste_shod'
