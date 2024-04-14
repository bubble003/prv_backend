from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    footer_table
)


class FooterResource(resources.ModelResource):
    class Meta:
        model = footer_table
        fields = ('id', 'key', 'value')
