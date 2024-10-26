# tarjeta\apps\maestros\forms\titulo_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Titulo
from diseno_base.diseno_bootstrap import (
	formclasstext, formclassselect)


class TituloForm(CrudGenericForm):
	
	class Meta:
		model = Titulo
		fields = '__all__'

		widgets = {
			'estatus_titulo': 
				forms.Select(attrs={**formclassselect}), 
			'titulo': 
				forms.TextInput(attrs={**formclasstext}),
		}


