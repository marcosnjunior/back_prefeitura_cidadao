from django import forms

from .models import Problema_iluminacao,Expansao_iluminacao,Tapa_buraco,GaleriaBocaLobo,Terraplanagem,Pinturas,Hidraulicos,Eletricos,Serralharia,Jardinagem,Mercenaria


class Problema_iluminacaoForm(forms.ModelForm):
    class Meta:
        model = Problema_iluminacao
        fields ='__all__'
        labels = {
            'tipo_iluminacao' : 'Tipo de Lâmpadas*',
            'qual_problema_iluminacao' : 'Qual e o Problema com a Iluminação',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro Do Problema*',
            'rua': 'Inserir A Rua*',
            'pontoReferencia' : 'Ponto de Referência*',
            'observacoes' : 'Observações',
            'telefone': 'Inserir Telefone/Whatsapp*',  
        }

class Expansao_iluminacaoForm(forms.ModelForm):
    class Meta:
        model = Expansao_iluminacao
        fields ='__all__'
        labels = {
            'pontoReferencia' : 'Ponto de Referência*',
            'expansao_iluminacao' : 'Expansão Iluminação',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro Do Problema*',
            'rua': 'Inserir A Rua*',
            'observacoes' : 'Observações',
            'telefone': 'Inserir Telefone/Whatsapp*',  
        }

class Tapa_buracoForm(forms.ModelForm):
    class Meta:
        model = Tapa_buraco
        fields ='__all__'
        labels = {
            'pontoReferencia' : 'Ponto de Referência*',
            'tipo_pavimentacao' : 'Expansão Iluminação',
            'observacoes' : 'Observações',
            'telefone': 'Inserir Telefone/Whatsapp*',
            'rua': 'Inserir A Rua*', 
            'numeroRecidencia': 'Número da Casa*', 
            'bairro' : 'Inserir Bairro Do Problema*',
            'estadoUF': 'Estado',
            'cidade' : 'Cidade*',
            'cep' : 'Inserir CEP*', 
        }

class GaleriaBocaLoboForm(forms.ModelForm):
    class Meta:
        model = GaleriaBocaLobo
        fields ='__all__'
        labels = {
            'pontoReferencia' : 'Ponto de Referência*',
            'problema_Drenagem' : 'Qual o Problema com a Drenagem?.*',
            'observacoes' : 'Observações',
            'telefone': 'Inserir Telefone/Whatsapp*',
            'rua': 'Inserir A Rua*', 
            'numeroRecidencia': 'Número da Casa*', 
            'bairro' : 'Inserir Bairro Do Problema*',
            'estadoUF': 'Estado',
            'cidade' : 'Cidade*',
            'cep' : 'Inserir CEP*', 
        }



class TerraplanagemForm(forms.ModelForm):
    class Meta:
        model = Terraplanagem
        fields ='__all__'
        labels = {
            'pontoReferencia' : 'Ponto de Referência*',
            'observacoes' : 'Observações',
            'telefone': 'Inserir Telefone/Whatsapp*',
            'rua': 'Rua*',
            'numeroRecidencia': 'Número da Casa*',
            'bairro' : 'Inserir Bairro*',
            'cidade' : 'Cidade*',
            'cep' : 'Inserir CEP*',
        }

class PinturasForm(forms.ModelForm):
    class Meta:
        model = Pinturas
        fields ='__all__'
        labels = {
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }

class HidraulicosForm(forms.ModelForm):
    class Meta:
        model = Hidraulicos
        fields ='__all__'
        labels = {
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }

class EletricosForm(forms.ModelForm):
    class Meta:
        model = Eletricos
        fields ='__all__'
        labels = {
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }

class SerralhariaForm(forms.ModelForm):
    class Meta:
        model = Serralharia
        fields ='__all__'
        labels = {
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }

class JardinagemForm(forms.ModelForm):
    class Meta:
        model = Jardinagem
        fields ='__all__'
        labels = {
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'cep' : 'Inserir CEP*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }

class MercenariaForm(forms.ModelForm):
    class Meta:
        model = Mercenaria
        fields ='__all__'
        labels = {
            'cep' : 'Inserir CEP*',
            'telefone': 'Inserir Telefone/Whatsapp*',
            'observacoes' : 'Observações',
            'pontoReferencia' : 'Ponto de Referência*',
            'bairro' : 'Inserir Bairro*',
            'nome_Area_publica': 'Nome Da Área Pública*',  
            'rua': 'Inserir A Rua*',
        }
