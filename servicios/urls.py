from django.contrib import admin
from django.urls import path, include
from .views import crearSiniestro, ordendePago, crearTercero


urlpatterns = [
    path('crearSiniestro', crearSiniestro ),
    path('ordendePago', ordendePago ),
    path('crearTercero', crearTercero ),
]