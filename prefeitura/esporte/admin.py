from django.contrib import admin
from .models import Recebimento_de_Convite, Solicitacao_de_Apoio, Solicitacao_de_Material,  Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos, Solicitacao_de_Uso_de_Espaco_Fisico

# Register your models here.

admin.site.register(Recebimento_de_Convite)
admin.site.register(Solicitacao_de_Apoio)
admin.site.register(Solicitacao_de_Material)
admin.site.register(Solicitacao_de_Reparos_e_Manutencao_de_Equipamentos)
admin.site.register(Solicitacao_de_Uso_de_Espaco_Fisico)
