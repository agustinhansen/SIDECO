from django import forms

from .models import Persona

#Formularios de registro de desempleado

class PostForm(forms.ModelForm):

    class Meta:
        model = Persona
        fields = ('DNI', 'tipo_de_trabajo')
