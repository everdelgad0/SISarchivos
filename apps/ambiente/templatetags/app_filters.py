from django import template
import os
from django.conf import settings
from django.utils.safestring import mark_safe
from ..models import Ambiente, Estante, Archivador, Archivo
from django.urls import reverse

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(obj, attr):
    return getattr(obj, attr, '')

@register.filter(name='split_path')
def split_path(path):
    return os.path.basename(str(path))

def get_cache_bust_url(file_field):
    if not file_field or not hasattr(file_field, 'path'):
        return file_field.url if file_field else ''
    
    try:
        mtime = int(os.path.getmtime(file_field.path))
        return f"{file_field.url}?v={mtime}"
    except (OSError, TypeError):
        return file_field.url

@register.filter(name='is_image')
def is_image(file_field):
    if not file_field:
        return False
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']
    file_name = file_field.name.lower()
    return any(file_name.endswith(ext) for ext in image_extensions) 

@register.filter(name='bust_cache_url')
def bust_cache_url(file_field):
    return get_cache_bust_url(file_field)

@register.filter
def get_full_path(obj):
    parts = []
    base_url_name = 'ambiente'
    try:
        if isinstance(obj, Archivo) and obj.archivador:
            estante = obj.archivador.estante
            ambiente = estante.ambiente
            parts.append(f'<span class="text-primary">{ambiente.nombre}</span>')
            parts.append(f'<span class="text-success">{estante.nombre}</span>')
            parts.append(f'<span class="text-info">{obj.archivador.nombre}</span>')

        elif isinstance(obj, Archivador) and obj.estante:
            ambiente = obj.estante.ambiente
            parts.append(f'<span class="text-primary">{ambiente.nombre}</span>')
            parts.append(f'<span class="text-success">{obj.estante.nombre}</span>')

        elif isinstance(obj, Estante) and obj.ambiente:
            parts.append(f'<span class="text-primary">{obj.ambiente.nombre}</span>')

        elif isinstance(obj, Ambiente):
            # Un ambiente no tiene ruta padre, así que no se muestra nada.
            pass

    except AttributeError:
        return ""

    if not parts:
        return ""
    path_html = ' <i class="fas fa-angle-right fa-xs mx-1 text-muted"></i> '.join(parts)
    return mark_safe(f'<span class="small text-muted">{path_html}</span>')