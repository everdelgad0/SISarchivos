from django import forms
from .models import *

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class AmbienteForm(BaseForm):
    class Meta:
        model = Ambiente
        fields = '__all__'

class EstanteForm(BaseForm):
    class Meta:
        model = Estante
        fields = ['nombre', 'descripcion']

class EstanteGeneralForm(BaseForm):
    class Meta:
        model = Estante
        fields = ['nombre', 'descripcion', 'ambiente']
    
class ArchivadorForm(BaseForm):
    class Meta:
        model = Archivador
        fields = ['nombre', 'descripcion']

class ArchivadorGeneralForm(BaseForm):
    class Meta:
        model = Archivador
        fields = ['nombre', 'descripcion', 'estante']

class ArchivoForm(BaseForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'descripcion', 'archivo']

class ArchivoGeneralForm(BaseForm):
    class Meta:
        model = Archivo
        fields = ['nombre', 'descripcion', 'archivo', 'archivador']