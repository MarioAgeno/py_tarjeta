# tarjeta\apps\maestros\forms\sucursal_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Sucursal
from diseno_base.diseno_bootstrap import (formclasstext, formclassselect)


class SucursalForm(CrudGenericForm):
	
	class Meta:
		model = Sucursal
		fields = '__all__'

		widgets = {
			'estatus_sucursal': 
				forms.Select(attrs={**formclassselect}), 
			'nombre_sucursal': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio_sucursal': 
				forms.TextInput(attrs={**formclasstext}),
			'localidad_sucursal': 
				forms.TextInput(attrs={**formclasstext}),
			'codigo_postal': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2': 
				forms.TextInput(attrs={**formclasstext}),
			'movil': 
				forms.TextInput(attrs={**formclasstext}),
			'mail': 
				forms.EmailInput(attrs={**formclasstext}),
			'ruta_archivo': 
				forms.TextInput(attrs={**formclasstext}),
		}

