# predictor/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),          # Página principal
    path('predict/', views.index, name='predict') # Usa la misma vista para POST
]
