from django import forms
from .models import UsuariosModel
class UsuarioForm(forms.ModelForm):
    class Meta:
        model = UsuariosModel
        fields = ['nome','login','senha']
        widgets = {
            'senha':forms.PasswordInput(),
        }