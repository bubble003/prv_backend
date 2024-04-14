from django.db import models
from disease.models import disease_table, pathy_table

class disease_analytics_table(models.Model):
    disease = models.ForeignKey(disease_table, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField(default=0)

class pathy_analytics_table(models.Model):
    pathy = models.ForeignKey(pathy_table, on_delete=models.CASCADE)
    date = models.DateField()
    count = models.IntegerField(default=0)


'''class Blog(models.Model):                      #for views count
    title=models.CharField(max_length=200)
    blog_views=models.IntegerField(default=0)'''

