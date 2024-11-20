from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name=''),
    path('visitUs', views.visitUs, name='visitUs'),
    path('visitEdu', views.visitEdu, name='visitEdu'),
    path('whatsHere', views.whatsHere, name='whatsHere'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('example', views.example, name='example'),

]
