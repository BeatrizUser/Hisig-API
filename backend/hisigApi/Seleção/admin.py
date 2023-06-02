from django.contrib import admin
from django.utils.html import format_html
from django.utils.text import Truncator
from .models import Empresa, Vaga, Candidato, Habilidade

class CandidatoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'vaga_interesse', 'habilidades_list', 'exibir_curriculo')

    def habilidades_list(self, obj):
        return ", ".join([habilidade.nome for habilidade in obj.habilidades.all()])
    
    def exibir_curriculo(self, obj):
        if obj.curriculo:
            return format_html('<a href="{}" target="_blank">Baixar Curriculo</a>', obj.curriculo.url)
        else:
            return ''

    habilidades_list.short_description = 'Habilidades'
    exibir_curriculo.short_description = 'Curriculo'

class VagaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'descricao_truncada', 'candidatos_inscritos')
    list_display_links = ('titulo',)  # Adiciona link para detalhes da vaga

    def descricao_truncada(self, obj):
        return Truncator(obj.descricao).chars(100)

    def candidatos_inscritos(self, obj):
        return obj.candidatos.count()
    

    descricao_truncada.short_description = 'Descrição'
    candidatos_inscritos.short_description = 'Candidatos Inscritos'

admin.site.register(Candidato, CandidatoAdmin)
admin.site.register(Empresa)
admin.site.register(Vaga, VagaAdmin)
admin.site.register(Habilidade)
