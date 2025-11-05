from django import forms
from .models import *

class AmbienteForm(forms.ModelForm):
    class Meta:
        model = Ambiente
        fields = '__all__'

class EstanteForm(forms.ModelForm):
    class Meta:
        model = Estante
        fields = '__all__'

class ArchivadorForm(forms.ModelForm): 
    class Meta:
        model = Archivador
        fields = '__all__'

class ArchivoForm(forms.ModelForm): 
    class Meta:
        model = Archivo
        fields = '__all__'