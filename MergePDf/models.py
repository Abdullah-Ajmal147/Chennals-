from pydoc import describe
import uuid
from django.db import models

# Create your models here.
# class fileuploader(models.Model):
#     file = models.FileUpload()
class modelA(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=20,)
    lastname = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.id)
    
class modelB(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    modela = models.ForeignKey(modelA, on_delete=models.CASCADE, related_name= 'modela')
    
    describe = models.CharField(max_length=50,null=True, blank=True)
    
    def __str__(self):
        return str(self.id)
    
    