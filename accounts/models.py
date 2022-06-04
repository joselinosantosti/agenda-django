from empregados.models import Empregado
from django import forms

class FormEmpregado(forms.ModelForm):
    class Meta:
        model = Empregado
        exclude = ('mostrar',)