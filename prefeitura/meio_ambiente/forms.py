from django import forms

from .models import Plantio_de_Arvores

class Plantio_de_ArvoreForm(forms.ModelForm):
    class Meta:
        model = Plantio_de_Arvores
        fields ='__all__'
        labels = {
            'larg_compr_calcada' : 'Largura X Comprimento da Calçada',
            'observacoes' : 'Observações',
            'cep' : 'CEP',
            'bairro' : 'Bairro',
            'nome_rua' : 'Nome da Rua',
            'ponto_refer' : 'Ponto de Referência'
        }

        