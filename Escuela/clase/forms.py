from django import forms

from . import models


class ClaseListForm(forms.ModelForm):
    class Meta:
        model = models.Comision
        fields = ["nombre", "curso", "profesor"]


class ClaseEstudianteForm(forms.ModelForm):
    class Meta:
        model = models.Estudiante
        fields = ["nombre"]