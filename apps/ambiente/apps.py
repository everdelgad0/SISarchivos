from django.apps import AppConfig


class AmbienteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.ambiente'
    
class EstanteConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.estante'
