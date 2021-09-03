from django.urls import path, include
from . import views
from django.views.static import serve 
from django.conf import settings
from django.conf.urls import  url

app_name = 'stegnograph'

urlpatterns = [
    path('', views.home,name='home'),
    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    # url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]