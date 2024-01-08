from django.contrib import admin

from .models import Tage, Foroosh


admin.site.register(Tage)



# @admin.register(Foroosh)
class ForooshAdmin(admin.ModelAdmin):
    list_display = ['shomare_factor', 'kharidar', 'geymat', 'daryafti','vazn_kol', 'total_metraje','mablag_kol', 'albagi_hesab', 'baste_shod']
    search_fields = ('shomare_factor', )
    list_filter = ('shomare_factor',)
    # prepopulated_fields = {'id':('shomare_factor',)}
    # raw_id_fields = ('id',)

admin.site.register(Foroosh, ForooshAdmin)



#
