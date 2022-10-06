from django.db import models

# Create your models here.
class data(models.Model):
    name = models.CharField(max_length=300)
    designation = models.CharField(max_length=100)
    perfession= models.CharField(max_length=100) 
