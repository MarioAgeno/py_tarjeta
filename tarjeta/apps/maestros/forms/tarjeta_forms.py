# tarjeta\apps\maestros\forms\tarjeta_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.tarjeta_models import Tarjeta
from diseno_base.diseno_bootstrap import (formclassdate,
	formclasstext, formclassselect, formclasscheck)

class TarjetaForm(CrudGenericForm):
	
	class Meta:
		model = Tarjeta
		fields = '__all__'

		widgets = {
			'estatus_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'id_sucursal_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_socio': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99999}),
			'adicional': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 99}),
			'digito_verificador': 
				forms.NumberInput(attrs={**formclasstext, 
							'min': 0, 'max': 9}),
			'numero_tarjeta':  
				forms.NumberInput(attrs={**formclasstext}), 
			'nombre_titular': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_localidad_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'id_provincia_tarjeta': 
				forms.Select(attrs={**formclassselect}), 
			'telefono_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'movil_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'mail_tarjeta': 
				forms.TextInput(attrs={**formclasstext}),
			'nombre_garantia': 
				forms.TextInput(attrs={**formclasstext}),
			'limite_maximo_tarjeta': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999999999, 'step': '0.01'}),
			'saldo_disponible': 
				forms.NumberInput(attrs={**formclasstext, 
                           'min': 0, 'max': 999999999, 'step': '0.01'}),
			'id_titulo': 
				forms.Select(attrs={**formclassselect}), 
			'id_tarjeta_estado': 
				forms.Select(attrs={**formclassselect}), 
			'fecha_alta': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'fecha_baja': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'vencimiento': 
				forms.TextInput(attrs={'type':'date', **formclassdate}),
			'liquidacion_mail': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'seguro': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'observacion': 
				forms.TextInput(attrs={**formclasstext}),
		
		}
