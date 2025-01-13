from django_filters.views import FilterView
from django.db.models import Sum
from ..forms.liquidacion_comercio_forms import LiquidacionComercioFilter
from ...maestros.models.comercio_models import LiquidacionComercio

# Liquidaciones a comercios tabla en pantalla
class LiquidacionComercioFilterView(FilterView):
    model = LiquidacionComercio
    filterset_class = LiquidacionComercioFilter
    template_name = 'listados/liquidacion_filter.html'
    context_object_name = 'liquidaciones'

    def get_paginate_by(self, queryset):
        return int(self.request.GET.get('paginate_by', 8))  # Valor predeterminado: 8

    def get_queryset(self):
        # Aplicar el filtro y obtener el queryset filtrado
        if not self.request.GET:
            return LiquidacionComercio.objects.none()  # Si no hay filtros, no devolver registros
        queryset = super().get_queryset()
        return queryset  # Devolver el queryset filtrado

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Opciones de paginación
        context['pagination_options'] = [8, 20, 50, 100]
        context['selected_pagination'] = int(self.request.GET.get('paginate_by', 8))
        context['query_params'] = self.request.GET.copy()
        context['query_params'].pop('page', None)  # Eliminar el parámetro de paginación para evitar conflictos

        # Cálculo de totales en base al queryset filtrado
        queryset = self.filterset_class(self.request.GET, queryset=self.model.objects.all()).qs
        context['totales'] = {
            'importe_liquidacion': queryset.aggregate(total=Sum('importe_liquidacion'))['total'] or 0,
            'importe_comision': queryset.aggregate(total=Sum('importe_comision'))['total'] or 0,
            'costo_financiero': queryset.aggregate(total=Sum('costo_financiero'))['total'] or 0,
            'retencion_ganancias': queryset.aggregate(total=Sum('retencion_ganancias'))['total'] or 0,
            'retencion_iva': queryset.aggregate(total=Sum('retencion_iva'))['total'] or 0,
            'retencio_ib': queryset.aggregate(total=Sum('retencio_ib'))['total'] or 0,
            'retencion_debito_credito': queryset.aggregate(total=Sum('retencion_debito_credito'))['total'] or 0,
            'total_liquidacion': queryset.aggregate(total=Sum('total_liquidacion'))['total'] or 0,
        }

        return context


from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa
from django.views.generic import View
from datetime import datetime

# Opcion para Reportes en PDF
class LiquidacionComercioPDFView(View):
    def get_queryset(self):
        if not self.request.GET:
            return LiquidacionComercio.objects.none()
        return LiquidacionComercioFilter(self.request.GET, queryset=LiquidacionComercio.objects.all()).qs

    def get_context_data(self):
        queryset = self.get_queryset()
        context = {
            'liquidaciones': queryset,
            'totales': {
                'importe_liquidacion': queryset.aggregate(total=Sum('importe_liquidacion'))['total'] or 0,
                'importe_comision': queryset.aggregate(total=Sum('importe_comision'))['total'] or 0,
                'costo_financiero': queryset.aggregate(total=Sum('costo_financiero'))['total'] or 0,
                'retencion_ganancias': queryset.aggregate(total=Sum('retencion_ganancias'))['total'] or 0,
                'retencion_iva': queryset.aggregate(total=Sum('retencion_iva'))['total'] or 0,
                'retencio_ib': queryset.aggregate(total=Sum('retencio_ib'))['total'] or 0,
                'retencion_debito_credito': queryset.aggregate(total=Sum('retencion_debito_credito'))['total'] or 0,
                'total_liquidacion': queryset.aggregate(total=Sum('total_liquidacion'))['total'] or 0,
            },
            'logo_path': 'static/img/logo_01.png',
            'filters': self.request.GET,  # Filtros en el encabezado
            'current_date': datetime.now().strftime('%d/%m/%Y'),
        }
        return context

    def generate_pdf(self, context):
        html = render_to_string('listados/liquidacion_pdf.html', context)
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reporte_liquidaciones.pdf"'

        pisa_status = pisa.CreatePDF(
            html, dest=response, encoding='UTF-8'
        )
        if pisa_status.err:
            return HttpResponse('Error al generar el PDF', status=500)
        return response

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.generate_pdf(context)
