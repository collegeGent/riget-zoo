from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name=''),
    path('visitUs', views.visitUs, name='visitUs'),
    path('visitEdu', views.visitEdu, name='visitEdu'),
    path('whatsHere', views.whatsHere, name='whatsHere'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('login', views.login, name='login'),
    path('sign-out', views.user_logout, name='sign-out'),
    path('register', views.register, name='register'),
    path('example', views.example, name='example'),

]
