from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, DetailView
from django.template.loader import get_template
from django.db.models import Q
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

class SearchResultsView(TemplateView):
    template_name = 'base/search_results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        if query:
            
            search_filter = Q(nombre__icontains=query)
            context['ambientes'] = Ambiente.objects.filter(search_filter)
            context['estantes'] = Estante.objects.filter(search_filter)
            context['archivadores'] = Archivador.objects.filter(search_filter)
            context['archivos'] = Archivo.objects.filter(search_filter)
            context['has_results'] = (context['ambientes'].exists() or context['estantes'].exists() or 
                                       context['archivadores'].exists() or context['archivos'].exists())
        return context


class AmbienteListView(ListView):
    model = Ambiente
    template_name = 'base/list.html' 
    paginate_by = 10 
    ordering = ['nombre'] 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'ambientes'
        context['model_name'] = 'Ambiente'
        context['model_name_plural'] = 'Ambientes'
        context['headers'] = ['nombre', 'descripción']
        context['fields'] = ['nombre', 'descripcion'] 
        context['detail_url_name'] = 'ambiente:ambiente_detail'
        context['create_url'] = reverse_lazy('ambiente:ambiente_create')
        context['update_url_name'] = 'ambiente:ambiente_update' 
        context['delete_url_name'] = 'ambiente:ambiente_delete' 
        context['children_list_url_name'] = 'ambiente:estante_list_by_ambiente' 
        context['children_model_name_plural'] = 'Estantes'
        return context

class AmbienteDetailView(DetailView):
    model = Ambiente
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'ambientes'
        context['title'] = f'Detalle de Ambiente: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        context['update_url_name'] = 'ambiente:ambiente_update'
        context['delete_url_name'] = 'ambiente:ambiente_delete'
        context['estante_count'] = self.object.estantes.count()
        context['children'] = self.object.estantes.all()
        context['child_model_name'] = 'Estante'
        context['child_model_name_plural'] = 'Estantes'
        context['child_headers'] = ['nombre', 'descripción']
        context['child_fields'] = ['nombre', 'descripcion']
        context['child_detail_url_name'] = 'ambiente:estante_detail'
        context['child_update_url_name'] = 'ambiente:estante_update'
        context['child_delete_url_name'] = 'ambiente:estante_delete'
        context['child_create_url'] = reverse_lazy('ambiente:estante_create', kwargs={'ambiente_pk': self.object.pk})

        # Breadcrumbs
        context['breadcrumbs'] = [
            {'name': self.object.nombre, 'active': True}
        ]
        return context

class AmbienteCreateView(CreateView):
    template_name = 'base/form.html' 
    form_class = AmbienteForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'ambientes'
        context['title'] = 'Crear Ambiente'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:ambiente_list')

class AmbienteUpdateView(UpdateView):
    template_name = 'base/form.html' 
    form_class = AmbienteForm
    model = Ambiente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'ambientes'
        context['title'] = f'Editar Ambiente: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': self.object.pk})

class AmbienteDeleteView(DeleteView):
    template_name = 'base/delete.html'
    model = Ambiente

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'ambientes'
        context['title'] = 'Borrar Ambiente'
        context['list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:ambiente_list')

class EstanteListAllView(ListView):
    model = Estante
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'estantes'
        context['model_name'] = 'Estante'
        context['model_name_plural'] = 'Estantes'
        context['headers'] = ['nombre', 'ambiente']
        context['fields'] = ['nombre', 'ambiente']
        context['detail_url_name'] = 'ambiente:estante_detail'
        context['create_url'] = reverse_lazy('ambiente:estante_create_general')
        context['update_url_name'] = 'ambiente:estante_update'
        context['delete_url_name'] = 'ambiente:estante_delete'
        context['children_list_url_name'] = 'ambiente:archivador_list_by_estante' 
        context['children_model_name_plural'] = 'Archivadores' 
        context['parent_model_name'] = 'ambiente' 
        return context

class EstanteDetailView(DetailView):
    model = Estante
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'estantes'
        context['title'] = f'Detalle de Estante: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': self.object.ambiente.pk})
        context['parent'] = self.object.ambiente
        context['update_url_name'] = 'ambiente:estante_update'
        context['delete_url_name'] = 'ambiente:estante_delete'
        context['children'] = self.object.archivadores.all()
        context['archivador_count'] = self.object.archivadores.count()
        context['child_model_name'] = 'Archivador'
        context['child_model_name_plural'] = 'Archivadores'
        context['child_headers'] = ['nombre', 'descripción']
        context['child_fields'] = ['nombre', 'descripcion']
        context['child_detail_url_name'] = 'ambiente:archivador_detail'
        context['child_update_url_name'] = 'ambiente:archivador_update'
        context['child_delete_url_name'] = 'ambiente:archivador_delete'
        context['child_create_url'] = reverse_lazy('ambiente:archivador_create', kwargs={'estante_pk': self.object.pk})
        context['breadcrumbs'] = [
            {'name': self.object.ambiente.nombre, 'url': reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': self.object.ambiente.pk})},
            {'name': self.object.nombre, 'active': True}
        ]
        return context

class EstanteListView(ListView):
    model = Estante
    template_name = 'base/list.html' 
    paginate_by = 10 
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ambiente_id = self.kwargs['pk']
        context['active_nav'] = 'ambientes'
        ambiente = get_object_or_404(Ambiente, pk=ambiente_id)
        context['model_name'] = 'Estante'
        context['model_name_plural'] = f'Estantes en {ambiente.nombre}'
        context['headers'] = ['nombre', 'ambiente']
        context['fields'] = ['nombre', 'ambiente']
        context['detail_url_name'] = 'ambiente:estante_detail'
        context['create_url'] = reverse_lazy('ambiente:estante_create', kwargs={'ambiente_pk': ambiente_id})
        context['update_url_name'] = 'ambiente:estante_update'
        context['delete_url_name'] = 'ambiente:estante_delete'
        context['children_list_url_name'] = 'ambiente:archivador_list_by_estante'
        context['children_model_name_plural'] = 'Archivadores'
        context['parent_list_url'] = reverse_lazy('ambiente:ambiente_list')
        return context

    def get_queryset(self):
        return super().get_queryset().filter(ambiente__id=self.kwargs['pk'])
        

class EstanteCreateView(CreateView):
    model = Estante
    template_name = 'base/form.html' 

    def get_form_class(self):
        if 'ambiente_pk' in self.kwargs:
            return EstanteForm
        return EstanteGeneralForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'ambiente_pk' in self.kwargs:
            context['active_nav'] = 'ambientes'
            ambiente = get_object_or_404(Ambiente, pk=self.kwargs['ambiente_pk'])
            context['title'] = f'Crear Estante en {ambiente.nombre}'
            context['list_url'] = reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.kwargs['ambiente_pk']})
        else:
            context['title'] = 'Crear Estante'
            context['active_nav'] = 'estantes'
            context['list_url'] = reverse_lazy('ambiente:estante_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': self.object.ambiente.pk})

    def form_valid(self, form):
        if 'ambiente_pk' in self.kwargs:
            ambiente = get_object_or_404(Ambiente, pk=self.kwargs['ambiente_pk'])
            form.instance.ambiente = ambiente
        return super().form_valid(form)

class EstanteUpdateView(UpdateView):
    model = Estante
    form_class = EstanteForm
    template_name = 'base/form.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'estantes'
        context['title'] = f'Editar Estante: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:estante_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:estante_detail', kwargs={'pk': self.object.pk})

class EstanteDeleteView(DeleteView):
    model = Estante
    template_name = 'base/delete.html' 
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'estantes'
        context['title'] = 'Borrar Estante'
        context['list_url'] = reverse_lazy('ambiente:estante_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': self.object.ambiente.pk})

class ArchivadorListView(ListView):
    model = Archivador
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        estante_id = self.kwargs['pk']
        context['active_nav'] = 'estantes'
        estante = get_object_or_404(Estante, pk=estante_id)
        context['model_name'] = 'Archivador'
        context['model_name_plural'] = f'Archivadores en {estante.nombre}'
        context['headers'] = ['nombre', 'estante']
        context['fields'] = ['nombre', 'estante']
        context['detail_url_name'] = 'ambiente:archivador_detail'
        context['create_url'] = reverse_lazy('ambiente:archivador_create', kwargs={'estante_pk': estante_id})
        context['update_url_name'] = 'ambiente:archivador_update'
        context['delete_url_name'] = 'ambiente:archivador_delete'
        context['children_list_url_name'] = 'ambiente:archivo_list_by_archivador'
        context['children_model_name_plural'] = 'Archivos'
        context['parent_list_url'] = reverse_lazy('ambiente:estante_list_by_ambiente', kwargs={'pk': estante.ambiente.pk})
        return context
    def get_queryset(self):
        return super().get_queryset().filter(estante__id=self.kwargs['pk'])

class ArchivadorDetailView(DetailView):
    model = Archivador
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivadores'
        context['title'] = f'Detalle de Archivador: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:estante_detail', kwargs={'pk': self.object.estante.pk})
        context['parent'] = self.object.estante
        context['update_url_name'] = 'ambiente:archivador_update'
        context['delete_url_name'] = 'ambiente:archivador_delete'
        context['children'] = self.object.archivos.all()
        context['archivo_count'] = self.object.archivos.count()
        context['child_model_name'] = 'Archivo'
        context['child_model_name_plural'] = 'Archivos'
        context['child_headers'] = ['nombre', 'descripción', 'archivo']
        context['child_fields'] = ['nombre', 'descripcion', 'archivo']
        context['child_detail_url_name'] = 'ambiente:archivo_detail'
        context['child_update_url_name'] = 'ambiente:archivo_update'
        context['child_delete_url_name'] = 'ambiente:archivo_delete'
        context['child_create_url'] = reverse_lazy('ambiente:archivo_create', kwargs={'archivador_pk': self.object.pk})
        ambiente = self.object.estante.ambiente
        estante = self.object.estante
        context['breadcrumbs'] = [
            {'name': ambiente.nombre, 'url': reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': ambiente.pk})},
            {'name': estante.nombre, 'url': reverse_lazy('ambiente:estante_detail', kwargs={'pk': estante.pk})},
            {'name': self.object.nombre, 'active': True}
        ]
        return context

class ArchivadorListAllView(ListView):
    model = Archivador
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivadores'
        context['model_name'] = 'Archivador'
        context['model_name_plural'] = 'Archivadores'
        context['headers'] = ['nombre', 'estante']
        context['fields'] = ['nombre', 'estante']
        context['detail_url_name'] = 'ambiente:archivador_detail'
        context['create_url'] = reverse_lazy('ambiente:archivador_create_general')
        context['update_url_name'] = 'ambiente:archivador_update'
        context['delete_url_name'] = 'ambiente:archivador_delete'
        context['children_list_url_name'] = 'ambiente:archivo_list_by_archivador' 
        context['children_model_name_plural'] = 'Archivos' 
        return context

class ArchivadorCreateView(CreateView):
    model = Archivador
    template_name = 'base/form.html'

    def get_form_class(self):
        if 'estante_pk' in self.kwargs:
            return ArchivadorForm
        return ArchivadorGeneralForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'estante_pk' in self.kwargs:
            context['active_nav'] = 'estantes'
            estante = get_object_or_404(Estante, pk=self.kwargs['estante_pk'])
            context['title'] = f'Crear Archivador en {estante.nombre}'
            context['list_url'] = reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.kwargs['estante_pk']})
        else:
            context['title'] = 'Crear Archivador'
            context['active_nav'] = 'archivadores'
            context['list_url'] = reverse_lazy('ambiente:archivador_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': self.object.estante.pk})

    def form_valid(self, form):
        if 'estante_pk' in self.kwargs:
            estante = get_object_or_404(Estante, pk=self.kwargs['estante_pk'])
            form.instance.estante = estante
        return super().form_valid(form)

class ArchivadorUpdateView(UpdateView):
    model = Archivador
    form_class = ArchivadorForm 
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivadores'
        context['title'] = f'Editar Archivador: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:archivador_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_detail', kwargs={'pk': self.object.pk})

class ArchivadorDeleteView(DeleteView):
    model = Archivador
    template_name = 'base/delete.html' 

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivadores'
        context['title'] = 'Borrar Archivador'
        context['list_url'] = reverse_lazy('ambiente:archivador_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:estante_detail', kwargs={'pk': self.object.estante.pk})

class ArchivoListAllView(ListView):
    model = Archivo
    template_name = 'base/list.html'
    paginate_by = 10
    ordering = ['nombre']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivos'
        context['model_name'] = 'Archivo'
        context['model_name_plural'] = 'Archivos'
        context['headers'] = ['nombre', 'archivador', 'archivo']
        context['fields'] = ['nombre', 'archivador', 'archivo']
        context['detail_url_name'] = 'ambiente:archivo_detail'
        context['create_url'] = reverse_lazy('ambiente:archivo_create_general')
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
        archivador_id = self.kwargs['pk']
        context['active_nav'] = 'archivadores'
        archivador = get_object_or_404(Archivador, pk=archivador_id)
        context['model_name'] = 'Archivo'
        context['model_name_plural'] = f'Archivos en {archivador.nombre}'
        context['headers'] = ['nombre', 'archivador', 'archivo'] 
        context['fields'] = ['nombre', 'archivador', 'archivo'] 
        context['detail_url_name'] = 'ambiente:archivo_detail'
        context['create_url'] = reverse_lazy('ambiente:archivo_create', kwargs={'archivador_pk': archivador_id})
        context['update_url_name'] = 'ambiente:archivo_update'
        context['delete_url_name'] = 'ambiente:archivo_delete'
        context['parent_list_url'] = reverse_lazy('ambiente:archivador_list_by_estante', kwargs={'pk': archivador.estante.pk})
        return context
    def get_queryset(self):
        return super().get_queryset().filter(archivador__id=self.kwargs['pk'])

class ArchivoDetailView(DetailView):
    model = Archivo
    template_name = 'base/detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivos'
        context['title'] = f'Detalle de Archivo: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:archivador_detail', kwargs={'pk': self.object.archivador.pk})
        context['parent'] = self.object.archivador
        context['update_url_name'] = 'ambiente:archivo_update'
        context['delete_url_name'] = 'ambiente:archivo_delete'
        context['is_file_detail'] = True 
        archivador = self.object.archivador
        estante = archivador.estante
        ambiente = estante.ambiente
        context['breadcrumbs'] = [
            {'name': ambiente.nombre, 'url': reverse_lazy('ambiente:ambiente_detail', kwargs={'pk': ambiente.pk})},
            {'name': estante.nombre, 'url': reverse_lazy('ambiente:estante_detail', kwargs={'pk': estante.pk})},
            {'name': archivador.nombre, 'url': reverse_lazy('ambiente:archivador_detail', kwargs={'pk': archivador.pk})},
            {'name': self.object.nombre, 'active': True}
        ]
        return context

class ArchivoCreateView(CreateView):
    model = Archivo
    template_name = 'base/form.html'

    def get_form_class(self):
        if 'archivador_pk' in self.kwargs:
            return ArchivoForm
        return ArchivoGeneralForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if 'archivador_pk' in self.kwargs:
            context['active_nav'] = 'archivadores'
            archivador = get_object_or_404(Archivador, pk=self.kwargs['archivador_pk'])
            context['title'] = f'Crear Archivo en {archivador.nombre}'
            context['list_url'] = reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.kwargs['archivador_pk']})
        else:
            context['title'] = 'Crear Archivo'
            context['active_nav'] = 'archivos'
            context['list_url'] = reverse_lazy('ambiente:archivo_list')
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivo_list_by_archivador', kwargs={'pk': self.object.archivador.pk})

    def form_valid(self, form):
        if 'archivador_pk' in self.kwargs:
            archivador = get_object_or_404(Archivador, pk=self.kwargs['archivador_pk'])
            form.instance.archivador = archivador
        return super().form_valid(form)

class ArchivoUpdateView(UpdateView):
    model = Archivo
    form_class = ArchivoForm
    template_name = 'base/form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivos'
        context['title'] = f'Editar Archivo: {self.object.nombre}'
        context['list_url'] = reverse_lazy('ambiente:archivo_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivo_detail', kwargs={'pk': self.object.pk})

class ArchivoDeleteView(DeleteView):
    model = Archivo
    template_name = 'base/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_nav'] = 'archivos'
        context['title'] = 'Borrar Archivo'
        context['list_url'] = reverse_lazy('ambiente:archivo_detail', kwargs={'pk': self.object.pk})
        return context

    def get_success_url(self):
        return reverse_lazy('ambiente:archivador_detail', kwargs={'pk': self.object.archivador.pk})
