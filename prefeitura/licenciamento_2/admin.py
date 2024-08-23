from django.contrib import admin
from .models import SEDRUB_Autorizacao_Uso_Solo_Comercial, Autorizacao_Uso_de_Solo_Eventual, Atualizacao_Cadatral_Dos_Quiosques
# from urls import tes

# Register your models here.

# admin.site.register()
admin.site.register(SEDRUB_Autorizacao_Uso_Solo_Comercial)
admin.site.register(Autorizacao_Uso_de_Solo_Eventual)
admin.site.register(Atualizacao_Cadatral_Dos_Quiosques)