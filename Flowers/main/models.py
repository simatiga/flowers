from django.db import models

# Create your models here.
class plant_ctg (models.Model):
        col1 = models.TextField()
        col2 = models.IntegerField()
        col3 = models.FloatField()
        col4 = models.TextField()
        col5 = models.TextField()
        
        
class plant_income(models.Model):
        col1 = models.TextField()
        col2 = models.TextField()
        col3 = models.IntegerField()
        col4 = models.IntegerField()
        col5 = models.IntegerField()
        col6 = models.IntegerField()
        col7 = models.FloatField()
