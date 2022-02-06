from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('fibo_post/', views.fibo_post),
    path('fibo_archive/', views.fibo_archive, name='fibo_archive'),
]
