from django import forms
from .models import Manupulation
import datetime

class EncodeForm(forms.ModelForm):
    class Meta:
        model = Manupulation
        fields = ('box_image_path','container_image_path')
         
class DecodeForm(forms.ModelForm):
    class Meta:
        model = Manupulation
        fields = ('encrypted_image_path',)