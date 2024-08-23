from django.contrib import admin
from .models import Problema_iluminacao,Expansao_iluminacao,Tapa_buraco,GaleriaBocaLobo,Terraplanagem,Pinturas,Hidraulicos,Eletricos,Serralharia,Jardinagem,Mercenaria,SEMOB_Apoio_Evento,SEMOB_Baixa_multa_transito_pagamento,SEMOB_Baixa_multa_transporte_pagamento,SEMOB_Baixa_multa_deferimento_recurso,SEMOB_Baixa_Certidoes_IPI_ICMS,SEMOB_Cadastro_Acompanhante_Escolar

class Problema_iluminacaoAdmin(admin.ModelAdmin):
    list_display = ("id","tipo_iluminacao","qual_problema_iluminacao","observacoes","bairro","rua","numeroRecidencia","cep","pontoReferencia","telefone") 

class Expansao_iluminacaoAdmin(admin.ModelAdmin):
    list_display = ("id","expansao_iluminacao","observacoes","bairro","rua","numeroRecidencia","cep","pontoReferencia","telefone","estadoUF") 

class Tapa_buracoAdmin(admin.ModelAdmin):
    list_display = ("id","tipo_pavimentacao","observacoes","bairro","rua","numeroRecidencia","cep","pontoReferencia","telefone","estadoUF") 

class GaleriaBocaLoboAdmin(admin.ModelAdmin):
    list_display = ("id","problema_Drenagem","observacoes","bairro","rua","numeroRecidencia","cep","pontoReferencia","telefone","estadoUF") 

class TerraplanagemAdmin(admin.ModelAdmin):
    list_display = ("id","observacoes","bairro","rua","numeroRecidencia","cep","pontoReferencia","telefone","estadoUF") 

class ManutencaoAdmin(admin.ModelAdmin):
    list_display = ("id","observacoes","bairro","rua","nome_Area_publica","cep","pontoReferencia","telefone") 

class MercenariaAdmin(admin.ModelAdmin):
    list_display = ("id","observacoes","bairro","rua","cep","pontoReferencia","telefone") 

admin.site.register(Problema_iluminacao,Problema_iluminacaoAdmin)
admin.site.register(Expansao_iluminacao,Expansao_iluminacaoAdmin)
admin.site.register(Tapa_buraco,Tapa_buracoAdmin)
admin.site.register(GaleriaBocaLobo,GaleriaBocaLoboAdmin)
admin.site.register(Terraplanagem,TerraplanagemAdmin)
admin.site.register(Pinturas,ManutencaoAdmin)
admin.site.register(Hidraulicos,ManutencaoAdmin)
admin.site.register(Eletricos,ManutencaoAdmin)
admin.site.register(Serralharia,ManutencaoAdmin)
admin.site.register(Jardinagem,ManutencaoAdmin)
admin.site.register(Mercenaria,MercenariaAdmin)
admin.site.register(SEMOB_Apoio_Evento)
admin.site.register(SEMOB_Baixa_multa_transito_pagamento)
admin.site.register(SEMOB_Baixa_multa_transporte_pagamento)
admin.site.register(SEMOB_Baixa_multa_deferimento_recurso)
admin.site.register(SEMOB_Baixa_Certidoes_IPI_ICMS)
admin.site.register(SEMOB_Cadastro_Acompanhante_Escolar)