from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def tecnologia(request):
    return render(request, 'core/tecnologia.html')

def seguridad(request):
    return render(request, 'core/seguridad.html')

def estacionamiento(request):
    return render(request, 'core/estacionamiento.html')

def recorridos(request):
    return render(request, 'core/recorridos.html')

def traduccion(request):
    return render(request, 'core/traduccion.html')

def facilidades(request):
    return render(request, 'core/facilidades.html')