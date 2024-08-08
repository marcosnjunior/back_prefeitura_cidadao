from django import forms
from .models import ColetaAnimaisMortos, ApreensaoAnimal, Denuncia

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
