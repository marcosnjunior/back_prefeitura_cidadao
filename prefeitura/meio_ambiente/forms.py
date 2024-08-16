from django import forms

from .models import Plantio_de_Arvores, Poda_de_Arvores

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

class Poda_de_ArvoresForm(forms.ModelForm):
    class Meta:
        model = Poda_de_Arvores
        fields = '__all__'
        labels = {
            'rua' : 'Rua',
            'numero' : 'Número',
            'bairro' : 'Bairro',
            'estado' : 'Estado',
            'cidade' : 'Cidade',
            'cep' : 'CEP',
            'ponto_refer' : 'Ponto de Referência',
            'observacoes' : 'Observações',
            'telefone' : 'Telefone'
        }

            
        
        