# tarjeta\apps\maestros\forms\parametro_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Parametro
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect, formclassdate)


class ParametroForm(CrudGenericForm):
	
	class Meta:
		model = Parametro
		fields = '__all__'

		widgets = {
			'gastos': 
				forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'tasa': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'punitorios': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'minimo':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'cierre_ultimo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'cierre_actual': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'cierre_proximo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento_ultimo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento_actual': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento_proximo': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'retencion_debito_credito': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_ib_general': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_ib': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_ib_minimo':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'retencion_ganancia': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_ganancia_nc': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_ganancia_minimo':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'retencion_ganancia_minimo_nc':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'retencion_iva': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_iva_nc': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'retencion_iva_minimo':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999999}),
			'retencion_iva_estacion_servicio': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'sello': 
				forms.NumberInput(attrs={**formclasstext,
							'min': 0, 'max': 999, 'step': '0.01'}),
			'seguro': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'dias_mora':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99}),
			'mensaje': 
				forms.TextInput(attrs={**formclasstext}),
			'gastos_mail':
                forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 9999999}),
			'codigo_roela':
                forms.TextInput(attrs={**formclasstext}),
		}
