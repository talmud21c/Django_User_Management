from django.contrib import admin
from .models import ESGData


@admin.register(ESGData)
class ESGDataAdmin(admin.ModelAdmin):
    pass