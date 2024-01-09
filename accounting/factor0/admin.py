from django.contrib import admin

from .models import Roll, Invoice


admin.site.register(Roll)



# @admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['invoice_number', 'client', 'amount', 'received','total_meter', 'total_meter','total_price', 'notـreceived', ]
    search_fields = ('invoice_number', )
    list_filter = ('invoice_number',)
    # prepopulated_fields = {'id':('invoice_number',)}
    # raw_id_fields = ('id',)

admin.site.register(Invoice, InvoiceAdmin)



#
