from django.urls import path, include
from . import views

app_name = 'stegnograph'

urlpatterns = [
    path('', views.home,name='home'),
    
]
