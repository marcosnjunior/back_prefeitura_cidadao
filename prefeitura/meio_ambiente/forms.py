from django import forms

from .models import Plantio_de_Arvores

class Plantio_de_ArvoreForm(forms.ModelForm):
    class Meta:
        model = Plantio_de_Arvores
        fields ='__all__'
        
        