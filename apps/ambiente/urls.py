from django.urls import path
from .views import *

urlpatterns = [ 
    path('ambientes/', AmbienteListView.as_view(), name='ambiente_list'),  
    path('ambientes/crear/', AmbienteCreateView.as_view(), name='ambiente_create'),
    path('ambientes/editar/<int:pk>/', AmbienteUpdateView.as_view(), name='ambiente_update'),
    path('ambientes/borrar/<int:pk>/', AmbienteDeleteView.as_view(), name='ambiente_delete'),

    path('ambiente/<int:pk>/estantes/', EstanteListView.as_view(), name='estante_list_by_ambiente'), 
    path('estantes/', EstanteListAllView.as_view(), name='estante_list'),
    path('estantes/crear/', EstanteCreateView.as_view(), name='estante_create'),
    path('estantes/editar/<int:pk>/', EstanteUpdateView.as_view(), name='estante_update'),
    path('estantes/borrar/<int:pk>/', EstanteDeleteView.as_view(), name='estante_delete'),

    path('estante/<int:pk>/archivadores/', ArchivadorListView.as_view(), name='archivador_list_by_estante'), 
    path('archivadores/', ArchivadorListAllView.as_view(), name='archivador_list'),
    path('archivadores/crear/', ArchivadorCreateView.as_view(), name='archivador_create'),
    path('archivadores/editar/<int:pk>/', ArchivadorUpdateView.as_view(), name='archivador_update'),
    path('archivadores/borrar/<int:pk>/', ArchivadorDeleteView.as_view(), name='archivador_delete'),

    path('archivador/<int:pk>/archivos/', ArchivoListView.as_view(), name='archivo_list_by_archivador'), 
    path('archivos/', ArchivoListAllView.as_view(), name='archivo_list'),
    path('archivos/crear/', ArchivoCreateView.as_view(), name='archivo_create'),
    path('archivos/editar/<int:pk>/', ArchivoUpdateView.as_view(), name='archivo_update'),
    path('archivos/borrar/<int:pk>/', ArchivoDeleteView.as_view(), name='archivo_delete'),
]
