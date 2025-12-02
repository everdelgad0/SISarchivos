from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import RegistroForm, ProfileUpdateForm
from apps.ambiente.models import Ambiente, Estante, Archivador, Archivo
from .models import Profile


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

class UserProfileView(LoginRequiredMixin, UpdateView):
    """
    Muestra y actualiza la página de perfil del usuario autenticado.
    """
    template_name = 'auth/profile.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        # Devuelve la instancia del perfil del usuario actual, creándola si no existe.
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Añadimos el objeto 'user' explícitamente para mayor claridad en la plantilla
        context['user_data'] = self.request.user
        return context

    def form_valid(self, form):
        # No guardamos el formulario directamente para evitar borrar la imagen.
        # En su lugar, comprobamos si se subió un nuevo archivo.
        if 'picture' in self.request.FILES:
            # Si hay un nuevo archivo, lo asignamos al perfil y guardamos el perfil.
            self.object.picture = self.request.FILES['picture']
            self.object.save()
        return super().form_valid(form)
