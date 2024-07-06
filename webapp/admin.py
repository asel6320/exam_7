from django.contrib import admin

# Register your models here.
from webapp.models import GuestBook


class GuestBookAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'guest_note', 'created_at', 'changed_at', 'status']
    list_display_links = ['id', 'name']
    list_filter = ['name', 'status']
    search_fields = ['name', 'status', 'email']
    fields = ['name', 'email', 'guest_note', 'status']
    readonly_fields = ['created_at', 'changed_at']




# Register your models here.
admin.site.register(GuestBook, GuestBookAdmin)
from django.contrib import admin

# Register your models here.
