from django.contrib import admin
from .models import ColetaDePoda, TerrenoSemConservacao, LimpezaDePropriosMunicipais, CataTreco,  DenunciaDeDescarteIrregularDeResiduos, ColetaDeResiduosDiversificados, VarricaoDeLogradourosPublicos, ColetaSeletiva, FalhaNaColetaDomiciliar, ColetaDeAnimaisMortos 

# Register your models here.

admin.site.register(ColetaDePoda)
admin.site.register(TerrenoSemConservacao)
admin.site.register(LimpezaDePropriosMunicipais)
admin.site.register(CataTreco)
admin.site.register(DenunciaDeDescarteIrregularDeResiduos)
admin.site.register(ColetaDeResiduosDiversificados)
admin.site.register(VarricaoDeLogradourosPublicos)
admin.site.register(ColetaSeletiva)
admin.site.register(FalhaNaColetaDomiciliar)
admin.site.register(ColetaDeAnimaisMortos)
