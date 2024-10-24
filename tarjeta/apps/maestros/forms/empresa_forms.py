# neumatic\apps\maestros\forms\empresa_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Empresa
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)


class EmpresaForm(CrudGenericForm):
	
	class Meta:
		model = Empresa
		fields = '__all__'

		widgets = {
			'estatus_empresa': 
				forms.Select(attrs={**formclassselect}), 
			'razon_social': 
				forms.TextInput(attrs={**formclasstext}),
			'nombre_empresa': 
				forms.TextInput(attrs={**formclasstext}),
			'domicilio': 
				forms.TextInput(attrs={**formclasstext}),
			'localidad': 
				forms.TextInput(attrs={**formclasstext}),
			'provincia': 
				forms.TextInput(attrs={**formclasstext}),
			'codigo_postal': 
				forms.TextInput(attrs={**formclasstext}),
			'iva': 
				forms.TextInput(attrs={**formclasstext}),
			'cuit':
				forms.TextInput(attrs={**formclasstext}),
			'ingreso_bruto': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono': 
				forms.TextInput(attrs={**formclasstext}),
			'telefono2': 
				forms.TextInput(attrs={**formclasstext}),
			'movil': 
				forms.TextInput(attrs={**formclasstext}),
			'mail': 
				forms.TextInput(attrs={**formclasstext}),
			'web': 
				forms.TextInput(attrs={**formclasstext}),
			'imagen': 
				forms.TextInput(attrs={**formclasstext}),
		}
