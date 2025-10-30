from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView, FormView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    
class AmbienteListView(ListView):
    model = Ambiente
    template_name = 'ambiente/list.html'
    paginate_by = 10

class AmbienteCreateView(CreateView):
    template_name = 'ambiente/create.html'
    form_class = AmbienteForm
    success_url = reverse_lazy('ambiente:ambiente_list')
class AmbienteUpdateView(UpdateView):
    template_name = 'ambiente/update.html'
    form_class = AmbienteForm
    success_url = reverse_lazy('ambiente:ambiente_list')
    model = Ambiente

class AmbienteDeleteView(DeleteView):
    template_name = 'ambiente/delete.html'
    model = Ambiente
    success_url = reverse_lazy('ambiente:ambiente_list')

class EstanteListView(ListView):
    model = Estante
    template_name = 'estante/list.html'
    paginate_by = 10

class EstanteCreateView(CreateView):
    model = Estante
    form_class = EstanteForm
    template_name = 'estante/create.html'
    success_url = reverse_lazy('estante:estante_list')
class EstanteUpdateView(UpdateView):
    model = Estante
    form_class = EstanteForm
    template_name = 'estante/update.html'
    success_url = reverse_lazy('estante:estante_list')
class EstanteDeleteView(DeleteView):
    model = Estante
    template_name = 'estante/delete.html'
    success_url = reverse_lazy('estante:estante_list')