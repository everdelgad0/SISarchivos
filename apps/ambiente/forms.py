from django import forms
from .models import *

class BaseForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            current_classes = field.widget.attrs.get('class', '')
            new_classes = current_classes.split()
            if 'form-control' not in new_classes:
                new_classes.append('form-control')
            field.widget.attrs['class'] = ' '.join(new_classes)

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