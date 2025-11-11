from django import template
import os
from django.conf import settings

register = template.Library()

@register.filter(name='get_attribute')
def get_attribute(obj, attr):
    return getattr(obj, attr, '')

def get_cache_bust_url(file_field):
    """Helper function to create a cache-busting URL."""
    if not file_field or not hasattr(file_field, 'path'):
        return file_field.url if file_field else ''
    
    try:
        # Get modification time and append it as a query parameter
        mtime = int(os.path.getmtime(file_field.path))
        return f"{file_field.url}?v={mtime}"
    except (OSError, TypeError):
        # Fallback if file doesn't exist or path is incorrect
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