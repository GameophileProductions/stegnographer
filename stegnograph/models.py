from django.db import models

# Create your models here.
class Manupulation(models.Model):
    hide_image = models.ImageField(upload_to="'media",blank=True)
    hide_inside  = models.ImageField(upload_to="'media",blank=True)
    encrypted_image = models.ImageField(upload_to="'media",blank=True)
    
    def __str__(self):
        return str(self.id)
    
    def delete(self,*args, **kwargs):
        hide_image.delete(save=False)
        hide_inside.delete(save=False)
        encrypted_image.delete(save=False)
        super().delete(*args, **kwargs)        