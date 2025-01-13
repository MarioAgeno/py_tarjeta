# tarjeta\apps\listados\forms\liquidacion_comercio_forms.py

import django_filters
from django import forms
from ...maestros.models.comercio_models import LiquidacionComercio, Comercio
from ...maestros.models.base_models import Sucursal
from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect)


'''
class LiquidacionComercioFilter(django_filters.FilterSet):
    fecha_inicio = django_filters.DateFilter(
        field_name="fecha_liquidacion",
        lookup_expr='gte',
        label="Fecha Desde",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control w-auto'
        })
    )
    fecha_fin = django_filters.DateFilter(
        field_name="fecha_liquidacion",
        lookup_expr='lte',
        label="Fecha Hasta",
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control w-auto'
        })
    )
    sucursal = django_filters.ModelChoiceFilter(
        queryset=Sucursal.objects.filter(estatus_sucursal=True),  # Solo sucursales activas
        field_name='id_comercio__id_sucursal',  # Relación a través del comercio
        label="Sucursal",
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    class Meta:
        model = LiquidacionComercio
        fields = ['sucursal', 'id_comercio', 'fecha_inicio', 'fecha_fin']
'''


class LiquidacionComercioFilter(django_filters.FilterSet):
    fecha_inicio = django_filters.DateFilter(
        field_name="fecha_liquidacion",
        lookup_expr='gte',
        label="Fecha Desde",
        widget=forms.TextInput(attrs={'type':'date', **formclassdate})
    )
    fecha_fin = django_filters.DateFilter(
        field_name="fecha_liquidacion",
        lookup_expr='lte',
        label="Fecha Hasta",
        widget=forms.TextInput(attrs={'type':'date', **formclassdate})
    )
    sucursal = django_filters.ModelChoiceFilter(
        queryset=Sucursal.objects.filter(estatus_sucursal=True),  # Solo sucursales activas
        field_name='id_comercio__id_sucursal',  # Relación a través del comercio
        label="Sucursal",
        widget=forms.Select(attrs={**formclassselect})
    )
    id_comercio = django_filters.ModelChoiceFilter(
        queryset=Comercio.objects.filter(estatus_comercio=True),  # Solo comercios activos
        label="Comercio",
        widget=forms.Select(attrs={**formclassselect})
    )

    class Meta:
        model = LiquidacionComercio
        fields = ['sucursal', 'id_comercio', 'fecha_inicio', 'fecha_fin']
