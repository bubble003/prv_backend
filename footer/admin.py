from django.contrib import admin
from .models import footer_table
from .resources import *
from import_export.admin import ImportExportModelAdmin, ExportMixin
# Register your models here.
class FooterAdmin(ImportExportModelAdmin):
    resource_class = FooterResource
    list_display = ("key", "value",)

admin.site.register(footer_table, FooterAdmin)