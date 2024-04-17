from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    effective_table,
    pathy_table,
)
class EffectiveResources(resources.ModelResource):
    title = fields.Field(
        column_name='title',
        attribute='title',
        widget=ForeignKeyWidget(pathy_table, field='pathy')
    )
    class Meta:
        model = effective_table
        fields = ('id','title','text','image','show')
class PathyResources(resources.ModelResource):
    class Meta:
        model = pathy_table
        fields = ('id','pathy','name','link','show')