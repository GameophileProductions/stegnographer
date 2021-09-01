from django.shortcuts import render,HttpResponse
from .models import Manupulation
from stegnographer.settings import  BASE_DIR, MEDIA_ROOT
from .mediator import *
import os

# Create your views here.

def home(request):
    if request.method == "POST":
        if request.POST['formtype'] == 'encode':
            box_image = request.FILES['image1']
            container_image = request.FILES['image2']
            item = Manupulation(box_image_path=box_image, container_image_path=container_image)
            item.save()
            path = os.path.join(MEDIA_ROOT,str(item.name),'encoded.tiff')
            encryption(
                    box_image_path=item.box_image_path.path,
                    container_image_path=item.container_image_path.path,
                    encryption_output_path=path)
            item.encrypted_image_path = f'{item.name}/encoded.tiff'
            
            return render(request, 'download.html', {'encrypted':'yes','media':item})
            
        else:
            encrypted_image = request.FILES['encrypted_image']
            item = Manupulation(encrypted_image_path=encrypted_image)
            item.save()
            path = os.path.join(MEDIA_ROOT,str(item.name),'decoded.tiff')
            decryption(encrypted_image_path=item.encrypted_image_path.path, decryption_output_path=path)
                
            item.box_image_path = f'{item.name}/decoded.tiff'
            return render(request, 'download.html', {'decrypted':'yes','media':item})
                
    empty_db()
    return render(request, "index.html")

def empty_db():
    import shutil
    items = Manupulation.objects.all()
    for item in items:            
        item.delete()
    
    if os.path.exists(os.path.join(BASE_DIR,'media')):
        shutil.rmtree(os.path.join(BASE_DIR,'media'))