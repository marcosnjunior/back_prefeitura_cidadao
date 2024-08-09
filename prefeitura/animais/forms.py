from django import forms
from .models import *

class ColetaAnimaisMortosForm(forms.ModelForm):
    class Meta:
        model = ColetaAnimaisMortos
        fields = '__all__'
        ANIMAL_De_GRANDE_PORTE = [
            ("Cavalo", "Cavalo"),
            ("Boi", "Boi"),
            ("Cabra", "Cabra"),
            ("Porco", "Porco")
        ]
    
class ApreensaoAnimalForm(forms.ModelForm):
    class Meta:
        model = ApreensaoAnimal
        fields = '__all__'
        ANIMAL_De_GRANDE_PORTE = [
            ("Cavalo", "Cavalo"),
            ("Boi", "Boi"),
            ("Cabra", "Cabra"),
            ("Porco", "Porco")
        ]
        
class DenunciaForm(forms.ModelForm):
    class Meta:
        model = Denuncia
        fields = '__all__'

class AgendaConsultaForm(forms.ModelForm):
    class Meta:
        model = AgendaConsulta
        fields = '__all__'
        ANIMAL_De_GRANDE_PORTE = [
            ("Cavalo", "Cavalo"),
            ("Boi", "Boi"),
            ("Cabra", "Cabra"),
            ("Porco", "Porco")
        ]

class AgendaCastracaoForm(forms.ModelForm):
    class Meta:
        model = AgendaCastracao
        fields = '__all__'
        ANIMAL_De_GRANDE_PORTE = [
        ("Cavalo", "Cavalo"),
        ("Boi", "Boi"),
        ("Porco", "Porco")
        ]
class HospitalVeterinarioForm(forms.ModelForm):
    class Meta:
        model = HospitalVeterinario
        fields = '__all__'
        ANIMAL_De_GRANDE_PORTE = [
            ("Cavalo", "Cavalo"),
            ("Boi", "Boi"),
            ("Cabra", "Cabra"),
            ("Porco", "Porco")
        ]