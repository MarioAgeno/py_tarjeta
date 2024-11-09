# tarjeta\apps\maestros\forms\liquidacion_socio_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.liquidacion_models import LiquidacionSocio
from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect)


class LiquidacionSocioForm(CrudGenericForm):
	
	class Meta:
		model = LiquidacionSocio
		fields = '__all__'

		widgets = {
			'id_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'numero_tarjeta': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999, 'step': '1.00'}),
			'comprobante': 
				forms.TextInput(attrs={**formclassdate}),
			'liquidacion_socio': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'cierre_anterior': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'cierre_actual': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'cierre_proximo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento_anterior': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento_proximo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'limite_tarjeta': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'saldo_anterior': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'pago_anterior': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'pago_minimo': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_seguro': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_gasto': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_interes': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_punitorio': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_sellado': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'importe_total': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'su_pago': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 9999999999}),
			'fecha_pago': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'sucursal_pago': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 99}),
		}
