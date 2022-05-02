from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from store.admin import ProductAdmin
from store.models import Product
from tags.models import TaggedItem


class TagInline(GenericTabularInline):
    autocomplete_fields = ['tag']
    model = TaggedItem
    min = 1
    max_num = 10
    extra = 0


class CustomerProductAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    search_fields = ['title']

admin.site.unregister(Product)
admin.site.register(Product, CustomerProductAdmin)
