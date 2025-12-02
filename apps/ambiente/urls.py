from django.urls import path
from .views import *
from django.contrib.auth.decorators import login_required, permission_required

app_name = 'ambiente'

urlpatterns = [
    path('search/', SearchResultsView.as_view(), name='search_results'),

    # urls para estante
    path('ambiente/<int:pk>/estantes/', login_required(EstanteListView.as_view()), name='estante_list_by_ambiente'), 
    path('estantes/<int:pk>/', login_required(EstanteDetailView.as_view()), name='estante_detail'),
    path('estantes/', login_required(EstanteListAllView.as_view()), name='estante_list'),
    path('estantes/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(EstanteCreateView.as_view())), name='estante_create_general'),
    path('ambiente/<int:ambiente_pk>/estante/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(EstanteCreateView.as_view())), name='estante_create'),
    path('estantes/editar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(EstanteUpdateView.as_view())), name='estante_update'),
    path('estantes/borrar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(EstanteDeleteView.as_view())), name='estante_delete'),

    # urls para ambiente
    path('ambientes/', login_required(AmbienteListView.as_view()), name='ambiente_list'),  
    path('ambientes/<int:pk>/', login_required(AmbienteDetailView.as_view()), name='ambiente_detail'),
    path('ambientes/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(AmbienteCreateView.as_view())), name='ambiente_create'),
    path('ambientes/editar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(AmbienteUpdateView.as_view())), name='ambiente_update'),
    path('ambientes/borrar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(AmbienteDeleteView.as_view())), name='ambiente_delete'),

    # urls para archivador
    path('estante/<int:pk>/archivadores/', login_required(ArchivadorListView.as_view()), name='archivador_list_by_estante'), 
    path('archivadores/<int:pk>/', login_required(ArchivadorDetailView.as_view()), name='archivador_detail'),
    path('archivadores/', login_required(ArchivadorListAllView.as_view()), name='archivador_list'),
    path('archivadores/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivadorCreateView.as_view())), name='archivador_create_general'),
    path('estante/<int:estante_pk>/archivador/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivadorCreateView.as_view())), name='archivador_create'),
    path('archivadores/editar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivadorUpdateView.as_view())), name='archivador_update'),
    path('archivadores/borrar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivadorDeleteView.as_view())), name='archivador_delete'),

    # urls para archivo 
    path('archivador/<int:pk>/archivos/', login_required(ArchivoListView.as_view()), name='archivo_list_by_archivador'), 
    path('archivos/<int:pk>/', login_required(ArchivoDetailView.as_view()), name='archivo_detail'),
    path('archivos/', login_required(ArchivoListAllView.as_view()), name='archivo_list'),
    path('archivos/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivoCreateView.as_view())), name='archivo_create_general'),
    path('archivador/<int:archivador_pk>/archivo/crear/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivoCreateView.as_view())), name='archivo_create'),
    path('archivos/editar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivoUpdateView.as_view())), name='archivo_update'),
    path('archivos/borrar/<int:pk>/', permission_required("users.ambiente", raise_exception=True)(login_required(ArchivoDeleteView.as_view())), name='archivo_delete'),
    path('archivos/<int:pk>/download/', download_archivo, name='archivo_download'),
]
