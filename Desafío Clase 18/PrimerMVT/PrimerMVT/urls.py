from django.contrib import admin
from django.urls import path

from familia.views import agregar_familiar, list_familiar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('agregar_familiar/', agregar_familiar, name = 'agregar_familiar'),
    path('list_familiares/', list_familiar, name = 'list_familiares'),
]
