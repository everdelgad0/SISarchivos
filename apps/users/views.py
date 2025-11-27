from django.shortcuts import render
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from .forms import RegistroForm
# Asumo que tus modelos están en la app 'ambiente' por las URLs en tu plantilla home.html
# Si están en otro lugar, ajusta la siguiente línea.
from apps.ambiente.models import Ambiente, Estante, Archivador, Archivo


class RegistroUsuario(CreateView):
    model = User
    template_name = "auth/register.html"
    form_class = RegistroForm
    success_url = reverse_lazy('users:login')

def main(request):
    # Contamos la cantidad de objetos para cada modelo
    ambiente_count = Ambiente.objects.count()
    estante_count = Estante.objects.count()
    archivador_count = Archivador.objects.count()
    archivo_count = Archivo.objects.count()

    # Creamos un diccionario de contexto para pasarlo a la plantilla
    context = {
        'ambiente_count': ambiente_count,
        'estante_count': estante_count,
        'archivador_count': archivador_count,
        'archivo_count': archivo_count,
    }
    return render(request, 'home.html', context)
