from django.urls import path
from .views import *

app_name = 'ambiente'
app_name = 'estante'
urlpatterns = [
    path('', AmbienteListView.as_view(), name='ambiente_list'),  
    path('createAmbiente/', AmbienteCreateView.as_view(), name='ambiente_create'),
    path('updateAmbiente/<int:pk>/', AmbienteUpdateView.as_view(), name='ambiente_update'),
    path('deleteAmbiente/<int:pk>/', AmbienteDeleteView.as_view(), name='ambiente_delete'),

    path('Estante', EstanteListView.as_view(), name='estante_list'),
    path('createEstante/', EstanteCreateView.as_view(), name='estante_create'),
    path('updateEstante/<int:pk>/', EstanteUpdateView.as_view(), name='estante_update'),
    path('deleteEstante/<int:pk>/', EstanteDeleteView.as_view(), name='estante_delete'),
]
