from django.contrib import admin

from .models import Roll, Invoice


admin.site.register(Roll)



# @admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['factor_number', 'client', 'geymat', 'daryafti','total_meter', 'total_meter','total_price', 'notـreceived', ]
    search_fields = ('factor_number', )
    list_filter = ('factor_number',)
    # prepopulated_fields = {'id':('factor_number',)}
    # raw_id_fields = ('id',)

admin.site.register(Invoice, InvoiceAdmin)



#
