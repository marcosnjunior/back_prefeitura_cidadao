from django import forms

from .models import Plantio_de_Arvores, Poda_de_Arvores, lancamento_de_agua_servidas, lancamento_esgoto, poluicao_sonora, corte_irregular_arvores, poluicao_atmosferica, invasao_area_preservacao_permanente

class Plantio_de_ArvoreForm(forms.ModelForm):
    class Meta:
        model = Plantio_de_Arvores
        fields ='__all__'
        labels = {
            'larg_compr_calcada' : 'Largura X Comprimento da Calçada *',
            'observacoes' : 'Observações',
            'cep' : 'CEP *',
            'bairro' : 'Bairro *',
            'nome_rua' : 'Nome da Rua *',
            'ponto_refer' : 'Ponto de Referência *'
        }

        widgets = {
            'larg_compr_calcada': forms.TextInput(attrs={'placeholder': '   Largura X Comprimento da sua calçada'}),
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'cep': forms.TextInput(attrs={'placeholder': '   CEP'}),
            'bairro': forms.TextInput(attrs={'placeholder': '   Bairro:'}),
            'nome_rua': forms.TextInput(attrs={'placeholder': '   Nome da rua'}),
            'ponto_refer': forms.TextInput(attrs={'placeholder': '   Ponto de Referência:'}),
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

        widgets = {
            'rua' : forms.TextInput(attrs={'placeholder' : '   Rua'}),
            'numero' : forms.TextInput(attrs={'placeholder' : '   Número'}),
            'bairro' : forms.TextInput(attrs={'placeholder' : '   Bairro'}),
            'estado' : forms.TextInput(attrs={'placeholder' : '   Estado'}),
            'cidade' : forms.TextInput(attrs={'placeholder' : '   Cidade'}),
            'cep' : forms.TextInput(attrs={'placeholder' : '   CEP'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de Referência'}),
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'telefone' : forms.TextInput(attrs={'placeholder' : '   Telefone'}),
        }
            
        

class lancamento_de_agua_servidasForm(forms.ModelForm):
    class Meta:  
        model = lancamento_de_agua_servidas
        fields = '__all__'
        labels = {
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *',
            'observacoes' : 'Observações'
        }

        widgets = {
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
        }

class lancamento_esgotoForm(forms.ModelForm):
    class Meta:  
        model = lancamento_esgoto
        fields = '__all__'
        labels = {
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *',
            'observacoes' : 'Observações'
        }

        widgets = {
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
        }


class poluicao_sonoraForm(forms.ModelForm):
    class Meta:  
        model = poluicao_sonora
        fields = '__all__'
        labels = {
            'observacoes' : 'Observações',
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *'
        }

        widgets = {
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
        }


class corte_irregular_arvoresForm(forms.ModelForm):
    class Meta:  
        model = corte_irregular_arvores
        fields = '__all__'
        labels = {
            'observacoes' : 'Observações',
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *'
        }

        widgets = {
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
        }

class poluicao_atmosfericaForm(forms.ModelForm):
    class Meta:  
        model = poluicao_atmosferica
        fields = '__all__'
        labels = {
            'observacoes' : 'Observações',
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *'
        }

        widgets = {
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
        }

class invasao_area_preservacao_permanenteForm(forms.ModelForm):
    class Meta:  
        model = invasao_area_preservacao_permanente
        fields = '__all__'
        labels = {
            'observacoes' : 'Observações',
            'cep_problema' : 'Insira o CEP do local do Problema *',
            'bairro_problema' : 'Insira o Bairro do Problema*',
            'rua_problema' : 'Insira a Rua do local do problema *',
            'ponto_refer' : 'Ponto de referência: *'
        }

        widgets = {
            'observacoes': forms.Textarea(attrs={'placeholder': '   Observações'}),
            'cep_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o CEP Do local do Problema'}),
            'bairro_problema' : forms.TextInput(attrs={'placeholder' : '   Insira o Bairro Do local do Problema'}),
            'rua_problema' : forms.TextInput(attrs={'placeholder' : '   Insira A Rua Do local do Problema'}),
            'ponto_refer' : forms.TextInput(attrs={'placeholder' : '   Ponto de referência'}),
        }

            
        
        