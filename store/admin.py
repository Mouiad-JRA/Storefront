from django.contrib import admin

from . import models


# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'unit_price']
    list_editable = ['unit_price']
    list_per_page = 10


class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'membership']
    list_editable = ['membership']
    ordering = ['first_name', 'last_name']
    list_per_page = 10


admin.site.register(models.Collection)
admin.site.register(models.Customer, CustomerAdmin)
admin.site.register(models.Product, ProductAdmin)
