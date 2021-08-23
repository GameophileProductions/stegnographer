from django.db import models
import datetime, os
from stegnographer.settings import BASE_DIR

# Create your models here.
class Manupulation(models.Model):
    dt = datetime.datetime.now()
    name = '{}{}{} {}{}{}'.format(dt.day,dt.month,dt.year, dt.hour, dt.minute, dt.second)
    box_image_path = models.ImageField(upload_to=name,blank=True)
    container_image_path  = models.ImageField(upload_to=name,blank=True)
    encrypted_image_path = models.ImageField(upload_to=name,blank=True)
    
    def __str__(self):
        return str(self.id)
    
    def delete(self,*args, **kwargs):
        self.box_image_path.delete(save=False)
        self.container_image_path.delete(save=False)
        self.encrypted_image_path.delete(save=False)
        super().delete(*args, **kwargs)        