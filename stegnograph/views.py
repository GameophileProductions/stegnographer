from django.shortcuts import render,HttpResponse, redirect
from .forms import EncodeForm,DecodeForm
from .models import Manupulation
from stegnographer.settings import  BASE_DIR, MEDIA_URL, MEDIA_ROOT
# from stegnographer.settings import BASE_DIR
from django.core.files import File
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
                item  = Manupulation.objects.get(id=data.id)
                path = os.path.join(MEDIA_ROOT,str(item.name),'encoded.tiff')
                print(path)
                encryption(
                    box_image_path=item.box_image_path.path,
                    container_image_path=item.container_image_path.path,
                    encryption_output_path=path)
                
                item.encrypted_image_path.save('encoded.jpeg', File(open(path, 'rb')))
                path =  os.path.join(MEDIA_URL,str(item.name),'encoded.jpeg')
                print(path)
                # item.delete()
                return render(request,'base.html', {'media_download': item})
            else:
                pass
    
    return render(request, "base.html", {'encodeform': EncodeForm(), 'decodeform': DecodeForm()})