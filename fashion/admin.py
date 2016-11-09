from django.contrib import admin
from .models import Items


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['name', 'units', 'description', 'purchase_date']

admin.site.register(Items, ItemsAdmin)
