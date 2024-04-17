from django.contrib import admin
from .models import members_table, key_value_table
from django.contrib import admin
from import_export import resources, fields
from import_export.admin import ImportExportModelAdmin, ExportMixin
from import_export.widgets import ForeignKeyWidget
from .models import (
members_table,
key_value_table,
)
from .resources import *

# from import_export.admin import ImportExportModelAdmin



class MembersAdmin(ImportExportModelAdmin):
    resource_file=MembersResources
    list_display = ("name","team",)
    search_fields = ("name",)
    list_filter = ("show","team")

class Key_valueAdmin(ImportExportModelAdmin):
    resource_file=KeyResources
    list_display = ("key","value",)




admin.site.register(members_table, MembersAdmin)
admin.site.register(key_value_table,Key_valueAdmin)


