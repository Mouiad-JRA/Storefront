from django.contrib import admin
from .models import Tag


class TageAdmin(admin.ModelAdmin):
    search_fields = ['label']


admin.site.register(Tag, TageAdmin)
