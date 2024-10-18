from django.apps import AppConfig


class MaestrosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.maestros'

    def ready(self):
        # Importamos explícitamente cada archivo de modelos
        import apps.maestros.models.base_gen_models
        import apps.maestros.models.base_models
        import apps.maestros.models.comercio_models
        import apps.maestros.models.compra_models
        import apps.maestros.models.liquidacion_models
        import apps.maestros.models.tarjeta_models
