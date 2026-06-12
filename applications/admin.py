from django.contrib import admin

from applications.models import Request


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = (
        'client_name',
        'phone',
        'email',
        'title',
        'status',
        'created_at',
    )
    list_filter = ('status',)
    search_fields = ('client_name', 'phone', 'email')
    readonly_fields = ('created_at',)
