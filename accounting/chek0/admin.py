from django.contrib import admin

from .models import Czech, Received

admin.site.register(Czech)


class ReceivedAdmin(admin.ModelAdmin):
    list_display = [ 'cash', 'tota_received']
admin.site.register(Received, ReceivedAdmin)
