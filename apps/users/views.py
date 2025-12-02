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

    context = {
        'ambiente_count': ambiente_count,
        'estante_count': estante_count,
        'archivador_count': archivador_count,
        'archivo_count': archivo_count,
    }
    return render(request, 'home.html', context)

class UserProfileView(LoginRequiredMixin, UpdateView):
    template_name = 'auth/profile.html'
    form_class = ProfileUpdateForm
    success_url = reverse_lazy('users:profile')

    def get_object(self):
        profile, created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_data'] = self.request.user
        return context

    def form_valid(self, form):
        if 'picture' in self.request.FILES:
            self.object.picture = self.request.FILES['picture']
            self.object.save()
        return super().form_valid(form)
