# tarjeta\apps\maestros\forms\comercio_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.comercio_models import Comercio
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect, formclasscheck)


class ComercioForm(CrudGenericForm):
	
	class Meta:
		model = Comercio
		fields = '__all__'

		widgets = {
			'estatus_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_comercio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999999}),
			'pin': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 999}),
			'razon_social_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'nombre_titular': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_localidad_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'id_provincia_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'telefono_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'movil_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'mail_comercio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_actividad': 
				forms.Select(attrs={**formclassselect}), 
			'id_sucursal_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_socio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999}),
			'id_iva_comercio': 
				forms.Select(attrs={**formclassselect}), 
			'cuit_comercio':
				forms.NumberInput(attrs={**formclasstext}),
			'ingreso_bruto': 
				forms.TextInput(attrs={**formclasstext}),
			'monto_fijo': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'exento_ganancias': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'estacion_servicio': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'debito_credito': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'acreditar_cuenta': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'leido': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'mensaje': 
				forms.TextInput(attrs={**formclasstext}),
			'porcentaje_consumo': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
			'porcentaje_retencion_ib': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999, 'step': '0.01'}),
		}
