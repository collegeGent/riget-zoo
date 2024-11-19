from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path('',views.home, name=''),
    path('example', views.example, name='example')

]
