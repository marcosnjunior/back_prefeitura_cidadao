from django import forms
from saude.models import Vacinacao_Domiciliar
      
class VacinacaoDomiciliarForm(forms.ModelForm):
    class Meta:
        model = Vacinacao_Domiciliar
        fields = '__all__'
        labels = {
            'telefone': 'Telefone',
            'cep': 'CEP',
            'bairro': 'Bairro',
            'rua': 'Rua',
            'numeroCasa': 'Número da Casa',
            'pontoReferencia': 'Ponto de Referência',
            'dataNascimento': 'Data de Nascimento',
        }

        widgets = {
            'cep': forms.TextInput(attrs={'placeholder': '00000-000', 'pattern': '\d{5}-\d{3}'}),
            'bairro': forms.TextInput(attrs={'placeholder': 'Bairro'}),
            'rua': forms.TextInput(attrs={'placeholder': 'Rua'}),
            'pontoReferencia': forms.TextInput(attrs={'placeholder': 'Ponto de Referência'}),
            'numeroCasa': forms.NumberInput(attrs={'min': 0}),
            'telefone': forms.TextInput(attrs={'placeholder': '(__) _____-____', 'type': 'tel', 'maxlength': 15}),
            'dataNascimento': forms.DateInput(attrs={'type': 'date'}),
            'status': forms.TextInput(attrs={'type': 'hidden'}),
        }
        