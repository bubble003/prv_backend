from import_export import resources, fields
from import_export.widgets import ForeignKeyWidget
from .models import (
    disease_table,
    pathy_table,
    summary_table,
    data_table,
    source_table,
    case_table,
    sex_table,
    book_table,
    whatsapp_table,
)



class DiseaseResource(resources.ModelResource):
    class Meta:
        model = disease_table
        fields = ('id','name','show','text','summary','image_link')

class PathyResource(resources.ModelResource):
    disease = fields.Field(
        column_name='disease',
        attribute='disease',
        widget=ForeignKeyWidget(disease_table, field='name')
    )

    class Meta:
        model = pathy_table
        fields = ('id','disease','name','show','type')

class SourceResource(resources.ModelResource):
    class Meta:
        model = source_table
        fields = ('id','name','text','show')

class SexResource(resources.ModelResource):
    class Meta:
        model = sex_table
        fields = ('id','sex','show')

class BookResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, 'name')
    )

    disease = fields.Field(
        column_name='disease',
        attribute='get_disease_name',
    )

    def get_disease_name(self, obj):
        logger.debug('Debug message here')
        disease_name = ''
        if obj.pathy:
            disease_name = obj.pathy.disease.name
        return disease_name

    def init_instance(self, row=None):
        instance = super(BookResource, self).init_instance(row)
        print(f'Instance: {instance}')
        if instance and not instance.disease:
            instance.disease = self.get_disease_name(instance)
            print(f'Disease Name: {instance.disease}')
        return instance

    class Meta:
        model = book_table
        fields = ('id', 'pathy', 'show', 'name', 'author', 'rating', 'text', 'image_link', 'buy_link', 'disease')

class SummaryResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    class Meta:
        model = summary_table
        fields = ('id','pathy','summary')

class DataResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    source = fields.Field(
        column_name='source',
        attribute='source',
        widget=ForeignKeyWidget(data_table, field='name')
    )

    class Meta:
        model = book_table
        fields = ('id', 'pathy', 'source', 'show', 'title','link','summary','rating','comment')

class CaseResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    sex = fields.Field(
        column_name='source',
        attribute='source',
        widget=ForeignKeyWidget(sex_table, field='sex')
    )

    class Meta:
        model = case_table
        fields = ('id', 'pathy', 'title','summary', 'rating', 'comment', 'first_name', 'last_name', 'sex', 'age', 'occupation', 'email_address', 'phone_number', 'street_address','zip_code','state','country','history_link','allergies_link','reports_links','show','show_name','show_email','show_phone_number','show_address')

class WhatsappResource(resources.ModelResource):
    pathy = fields.Field(
        column_name='pathy',
        attribute='pathy',
        widget=ForeignKeyWidget(pathy_table, field='name')
    )

    class Meta:
        model = whatsapp_table
        fields = ('id','pathy','link','show')


