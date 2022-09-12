from django.contrib import admin
from django.urls import path
from proyecto1.views import *

urlpatterns=[
    path("admin/", admin.site.urls),
    path("saludar/", saludo),
    path('sumar/',sumar),
    path("name/<nombre>", miNombre),
    path("plantilla/", probandoTemplate),
]