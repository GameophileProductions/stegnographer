from django.shortcuts import render,HttpResponse, redirect
from .forms import EncodeForm,DecodeForm
from .models import Manupulation
from stegnographer.settings import MEDIA_ROOT, BASE_DIR, MEDIA_URL
from .mediator import *
import PIL.Image
import os
from PIL import ImageTk as itk
# Create your views here.
def home(request):
    if request.method == "POST":
        form_type = ''
        if request.POST.get('formtype') == 'encode':
            form = EncodeForm(request.POST, request.FILES)
            form_type = 'encode'
        else:
            form = DecodeForm(request.POST, request.FILES)
            form_type = 'decode'
            
        if form.is_valid():
            data = form.save()
            if form_type == 'encode':
                obj = Manupulation.objects.get(id=data.id)
                box_image_path = obj.box_image_path.path
                container_image_path = obj.container_image_path.path
                
                box_image = PIL.Image.open(mode='r', fp=box_image_path)
                container_image = PIL.Image.open(mode='r', fp=container_image_path)
                encode(box_image, container_image, 2).save(os.path.join(BASE_DIR,'media',str(obj.name),'encoded.tiff'))
                obj.encrypted_image_path = f'{obj.name}\encoded.tiff'
                
                return render(request,'base.html',{'image_download': obj.encrypted_image_path.url})
            else:
                pass
               
    return render(request, "base.html", {'encodeform': EncodeForm(), 'decodeform': DecodeForm()})