from django.contrib import admin
from django.urls import path
from .views import UserRegistration,LoginView
from django.views.generic import TemplateView
urlpatterns = [
   path("",TemplateView.as_view(template_name="home.html"),name="home"),
   path("reg",UserRegistration.as_view(),name="reg"),
   path("log",LoginView.as_view(),name="login")
]
