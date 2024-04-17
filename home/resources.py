from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    testimonial_table,
    video_table,
    key_value_table,
)


class TestimonialResource(resources.ModelResource):
    class Meta:
        model = testimonial_table
        fields = ('id', 'heading', 'text', 'name', 'location', 'show')


class VideoResource(resources.ModelResource):
    class Meta:
        model = video_table
        fields = ('id', 'heading', 'image', 'ytplaylist_link', 'show')


class KeyValueResource(resources.ModelResource):
    class Meta:
        model = key_value_table
        fields = ('id', 'key', 'value')
