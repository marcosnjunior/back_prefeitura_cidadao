from django import forms
from saude.models import Denuncia

class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'
        labels = {
            'tipo': 'Tipo de Estabelecimento',
            'horarioFuncionamento': 'Horário de Funcionamento',
            'endereco': 'Endereço',
            'bairro': 'Bairro',
            'pontoReferencia': 'Ponto de Referência',
            'motivoDenuncia': 'Motivo da Denúncia',
            'cidadeDaDenuncia': 'Cidade da Denúncia',
            'horaDaDenuncia': 'Hora da Denúncia',
            'status': 'Status',
        }

        widgets = {
            'tipo': forms.TextInput(attrs={'placeholder': 'Tipo de Estabelecimento'}),
            'endereco': forms.TextInput(attrs={'placeholder': 'Endereço'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'motivoDenuncia': forms.Textarea(attrs={'placeholder': 'Motivo da Denúncia'}),
            'cidadeDaDenuncia': forms.TextInput(attrs={'placeholder': 'Cidade da Denúncia'}),
            'horarioFuncionamento': forms.TextInput(attrs={'type': 'time', 'placeholder': '00:00'}),
            'horaDaDenuncia': forms.TextInput(attrs={'type': 'time', 'placeholder': '00:00'}),
            'pontoReferencia': forms.TextInput(attrs={'placeholder': 'Ponto de Referência'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }
  