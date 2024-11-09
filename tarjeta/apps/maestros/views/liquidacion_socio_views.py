# tarjeta\apps\maestros\views\liquidacion_socio_views.py
from django.urls import reverse_lazy
from ..views.cruds_views_generics import *
from django.views.generic import ListView
from ..models.liquidacion_models import LiquidacionSocio
from ..forms.liquidacion_socios_forms import LiquidacionSocioForm
from django.db.models import Q
from datetime import datetime


class LiquidacionSocioListView(ListView):
    model = LiquidacionSocio

	# Aplicación asociada al modelo
    app_label = model._meta.app_label
	
    #-- Usar esta forma cuando el modelo esté compuesto por más de una palabra: Ej. TipoCambio colocar "tipo_cambio".
    model_string = "liquidacion_socio"

	# Vistas del CRUD del modelo
    list_view_name = f"{model_string}_list"

	# Plantilla para crear o actualizar el modelo
    template_form = f"{app_label}/{model_string}_form.html"
    #template_name = '/apps/maestros/templates/maestros/liquidacion_socio_form.html'

	# Plantilla de la lista del CRUD
    template_list = f'{app_label}/maestro_list.html'

	# Nombre de la url 
    success_url = reverse_lazy(list_view_name)

    context_object_name = 'liquidaciones'
    ordering = ['-liquidacion_socio']  # Orden descendente por número de liquidación

    def get_queryset(self):
        queryset = super().get_queryset()
        
        # Búsquedas y filtros
        numero_tarjeta = self.request.GET.get('numero_tarjeta')
        id_tarjeta = self.request.GET.get('id_tarjeta')
        liquidacion = self.request.GET.get('liquidacion')
        sucursal_pago = self.request.GET.get('sucursal_pago')
        fecha_inicio = self.request.GET.get('fecha_inicio')
        fecha_fin = self.request.GET.get('fecha_fin')

        if numero_tarjeta:
            queryset = queryset.filter(numero_tarjeta=numero_tarjeta)
        if id_tarjeta:
            queryset = queryset.filter(id_tarjeta=id_tarjeta)
        if liquidacion:
            queryset = queryset.filter(liquidacion_socio=liquidacion)
        if sucursal_pago:
            queryset = queryset.filter(sucursal_pago=sucursal_pago)
        if fecha_inicio and fecha_fin:
            queryset = queryset.filter(cierre_actual__range=[fecha_inicio, fecha_fin])
        elif fecha_inicio:
            queryset = queryset.filter(cierre_actual__gte=fecha_inicio)
        elif fecha_fin:
            queryset = queryset.filter(cierre_actual__lte=fecha_fin)
        
        return queryset
