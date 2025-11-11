from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView
from .models import *
from .forms import *
from django.urls import reverse_lazy

# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['ambiente_count'] = Ambiente.objects.count()
        context['estante_count'] = Estante.objects.count()
        context['archivador_count'] = Archivador.objects.count()
        context['archivo_count'] = Archivo.objects.count()
        return context

class AmbienteListView(ListView):
    model = Ambiente
    template_name = 'base/list.html' 
    paginate_by = 10 
    ordering = ['nombre'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Ambiente'
        context['model_name_plural'] = 'Ambientes'
        context['headers'] = ['nombre', 'descripción']
        context['fields'] = ['nombre', 'descripcion']
        context['create_url'] = reverse_lazy('ambiente:ambiente_create') # Mismo namespace
        context['update_url_name'] = 'ambiente:ambiente_update' # Mismo namespace
        context['delete_url_name'] = 'ambiente:ambiente_delete' # Mismo namespace
        context['children_list_url_name'] = 'ambiente:estante_list_by_ambiente' # Nuevo nombre de ruta
        context['children_model_name_plural'] = 'Estantes'
        return context

class AmbienteCreateView(CreateView):
    template_name = 'base/form.html' 
    form_class = AmbienteForm
    success_url = reverse_lazy('ambiente:ambiente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Ambiente'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

class AmbienteUpdateView(UpdateView):
    template_name = 'base/form.html' 
    form_class = AmbienteForm
    success_url = reverse_lazy('ambiente:ambiente_list')
    model = Ambiente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Ambiente: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

class AmbienteDeleteView(DeleteView):
    template_name = 'base/delete.html'
    model = Ambiente
    success_url = reverse_lazy('ambiente:ambiente_list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Ambiente'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

class EstanteListAllView(ListView):
    model = Estante
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Estante'
        context['model_name_plural'] = 'Estantes'
        context['headers'] = ['nombre', 'ambiente']
        context['fields'] = ['nombre', 'ambiente']
        context['create_url'] = reverse_lazy('ambiente:estante_create')
        context['update_url_name'] = 'ambiente:estante_update'
        context['delete_url_name'] = 'ambiente:estante_delete'
        context['children_list_url_name'] = 'ambiente:archivador_list_by_estante' # Añadido
        context['children_model_name_plural'] = 'Archivadores' # Añadido
        return context

class EstanteListView(ListView):
    model = Estante
    template_name = 'base/list.html' 
    paginate_by = 10 
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Estante'
        context['model_name_plural'] = 'Estantes'
        context['headers'] = ['nombre', 'ambiente']
        context['fields'] = ['nombre', 'ambiente']
        context['create_url'] = reverse_lazy('ambiente:estante_create')
        context['update_url_name'] = 'ambiente:estante_update'
        context['delete_url_name'] = 'ambiente:estante_delete'
        context['children_list_url_name'] = 'ambiente:archivador_list_by_estante'
        context['children_model_name_plural'] = 'Archivadores'
        return context
    def get_queryset(self):
        return super().get_queryset().filter(ambiente__id=self.kwargs['pk'])
        

class EstanteCreateView(CreateView):
    model = Estante
    form_class = EstanteForm
    template_name = 'base/form.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Estante'
        # No podemos saber a qué lista volver, así que volvemos al inicio.
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        # Redirige a la lista de estantes del ambiente al que pertenece el nuevo estante.
        return reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})

class EstanteUpdateView(UpdateView):
    model = Estante
    form_class = EstanteForm
    template_name = 'base/form.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Estante: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})

class EstanteDeleteView(DeleteView):
    model = Estante
    template_name = 'base/delete.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Estante'
        context['list_url'] = reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})

class ArchivadorListView(ListView):
    model = Archivador
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Archivador'
        context['model_name_plural'] = 'Archivadores'
        context['headers'] = ['nombre', 'estante']
        context['fields'] = ['nombre', 'estante']
        context['create_url'] = reverse_lazy('ambiente:archivador_create')
        context['update_url_name'] = 'ambiente:archivador_update'
        context['delete_url_name'] = 'ambiente:archivador_delete'
        context['children_list_url_name'] = 'ambiente:archivo_list_by_archivador'
        context['children_model_name_plural'] = 'Archivos'
        return context
    def get_queryset(self):
        return super().get_queryset().filter(estante__id=self.kwargs['pk'])

class ArchivadorListAllView(ListView):
    model = Archivador
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Archivador'
        context['model_name_plural'] = 'Archivadores'
        context['headers'] = ['nombre', 'estante']
        context['fields'] = ['nombre', 'estante']
        context['create_url'] = reverse_lazy('ambiente:archivador_create')
        context['update_url_name'] = 'ambiente:archivador_update'
        context['delete_url_name'] = 'ambiente:archivador_delete'
        context['children_list_url_name'] = 'ambiente:archivo_list_by_archivador' # Añadido
        context['children_model_name_plural'] = 'Archivos' # Añadido
        return context

class ArchivadorCreateView(CreateView):
    model = Archivador
    form_class = ArchivadorForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Archivador'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})

class ArchivadorUpdateView(UpdateView):
    model = Archivador
    form_class = ArchivadorForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Archivador: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})

class ArchivadorDeleteView(DeleteView):
    model = Archivador
    template_name = 'base/delete.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Archivador'
        context['list_url'] = reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})

class ArchivoListAllView(ListView):
    model = Archivo
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Archivo'
        context['model_name_plural'] = 'Archivos'
        context['headers'] = ['nombre', 'archivador', 'archivo']
        context['fields'] = ['nombre', 'archivador', 'archivo']
        context['create_url'] = reverse_lazy('ambiente:archivo_create')
        context['update_url_name'] = 'ambiente:archivo_update'
        context['delete_url_name'] = 'ambiente:archivo_delete'
        return context

class ArchivoListView(ListView):
    model = Archivo
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['model_name'] = 'Archivo'
        context['model_name_plural'] = 'Archivos'
        context['headers'] = ['nombre', 'archivador', 'archivo'] 
        context['fields'] = ['nombre', 'archivador', 'archivo'] 
        context['create_url'] = reverse_lazy('ambiente:archivo_create')
        context['update_url_name'] = 'ambiente:archivo_update'
        context['delete_url_name'] = 'ambiente:archivo_delete'
        return context
    def get_queryset(self):
        return super().get_queryset().filter(archivador__id=self.kwargs['pk'])

class ArchivoCreateView(CreateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Crear Archivo'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})

class ArchivoUpdateView(UpdateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = f'Editar Archivo: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})

class ArchivoDeleteView(DeleteView):
    model = Archivo
    template_name = 'base/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Borrar Archivo'
        context['list_url'] = reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})
