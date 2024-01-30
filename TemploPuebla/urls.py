from django.contrib import admin
from django.urls import path

from core.views import index, tecnologia, seguridad, estacionamiento, recorridos, traduccion, facilidades

urlpatterns = [
    path('', index, name='index'),
    path('tecnologia/', tecnologia, name='tecnologia'),
    path('seguridad/', seguridad, name='seguridad'),
    path('estacionamiento/', estacionamiento, name='estacionamiento'),
    path('recorridos/', recorridos, name='recorridos'),
    path('traduccion/', traduccion, name='traduccion'),
    path('facilidades/', facilidades, name='facilidades'),
    path('admin/', admin.site.urls),
]
