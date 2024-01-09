from django.contrib import admin

from .models import Czech, Received

admin.site.register(Czech)


class ReceivedAdmin(admin.ModelAdmin):
    list_display = ['id', 'cash', 'total_received', 'updated']
admin.site.register(Received, ReceivedAdmin)
