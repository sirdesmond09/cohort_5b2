from django.contrib import admin
from .models import Item

# Register your models here.

# admin.site.register(Item)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "date_added"]
    list_filter = ["date_added"]
    search_fields = ["name", "price"]
    list_editable = ["price"]