from django.conf import urls
from django.urls import path
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path('',views.EmailSender.as_view())
    
    
    
]
