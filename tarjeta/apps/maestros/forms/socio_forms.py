# tarjeta\apps\maestros\forms\socio_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.tarjeta_models import Socio
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect, formclassdate, formclasscheck)


class SocioForm(CrudGenericForm):
	
	class Meta:
		model = Socio
		fields = '__all__'

		widgets = {
			'estatus_socio': 
				forms.Select(attrs={**formclassselect}), 
			'id_sucursal_socio': 
				forms.Select(attrs={**formclassselect}), 
			'codigo_socio': 
				forms.NumberInput(attrs={**formclasstext, 'min': 0, 'max': 99999}),
			'nombre_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_localidad_socio': 
				forms.Select(attrs={**formclassselect}), 
			'id_provincia_socio': 
				forms.Select(attrs={**formclassselect}), 
			'telefono_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'movil_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'mail_socio': 
				forms.TextInput(attrs={**formclasstext}),
			'id_tipo_documento_identidad': 
				forms.Select(attrs={**formclassselect}), 
			'numero_documento':
				forms.NumberInput(attrs={**formclasstext}),
			'cuit_socio':
				forms.NumberInput(attrs={**formclasstext}),
			'fecha_nacimiento': 
				forms.TextInput({'type':'date', **formclassdate}),
			'nacionalidad': 
				forms.TextInput(attrs={**formclasstext}),
			'id_actividad': 
				forms.Select(attrs={**formclassselect}), 
			'tipo_persona': 
				forms.Select(attrs={**formclassselect}), 
			'pep': 
				forms.CheckboxInput(attrs={**formclasscheck}),
			'fecha_ingreso': 
				forms.TextInput({'type':'date', **formclassdate}),
		}
