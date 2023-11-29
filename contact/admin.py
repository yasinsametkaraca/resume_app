from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'message', 'created_at')
    list_filter = ('created_at', )
    search_fields = ('name', 'email', 'subject', 'message')
    date_hierarchy = 'created_at'
    ordering = ('-created_at', )
    readonly_fields = ('name', 'email', 'subject', 'message', 'created_at')

    class Meta:
        model = Message
