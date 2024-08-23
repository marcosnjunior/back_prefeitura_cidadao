from django import forms
from saude.models import CartaoSus

class CartaoSUSForm(forms.ModelForm):
    class Meta:
        model = CartaoSus
        fields = '__all__'
        labels = {
            'nome': 'Nome Completo',
            'cor': 'Qual é a sua raça/cor?',
        }

