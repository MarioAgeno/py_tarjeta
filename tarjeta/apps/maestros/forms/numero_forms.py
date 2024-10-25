# tarjeta\apps\maestros\forms\numero_forms.py
from django import forms
from .crud_forms_generics import CrudGenericForm
from ..models.base_models import Numero
from diseno_base.diseno_bootstrap import (formclassselect, formclasstext)


class NumeroForm(CrudGenericForm):
	
	class Meta:
		model = Numero
		fields = '__all__'

		widgets = {
			'estatus_numero': 
				forms.Select(attrs={**formclassselect}),
			'cupon': 
				forms.NumberInput(attrs={**formclasstext,
                           'min': 0, 'max': 999999}),
		}
