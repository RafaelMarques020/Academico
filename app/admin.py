from django.contrib import admin
from .models import *

class PessoaInline(admin.TabularInline):
    model = Pessoa
    extra = 1

class CursoInline(admin.TabularInline):
    model = Curso
    extra = 1

class DisciplinaInline(admin.TabularInline):
    model = CursoDisciplina
    extra = 1

class AvaliacaoInline(admin.TabularInline):
    model = Avaliacao
    extra = 1


class CidadeAdmin(admin.ModelAdmin):
    list_display = ('nome', 'uf')

class OcupacaoAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [PessoaInline] 

class InstituicaoEnsinoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'cidade')
    inlines = [CursoInline] 

class AreaSaberAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    inlines = [CursoInline] 

class CursoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'carga_horaria_total', 'instituicao')
    inlines = [DisciplinaInline]

class DisciplinaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'area_saber')
    inlines = [AvaliacaoInline] 


admin.site.register(Cidade, CidadeAdmin)
admin.site.register(Ocupacao, OcupacaoAdmin)
admin.site.register(InstituicaoEnsino, InstituicaoEnsinoAdmin)
admin.site.register(AreaSaber, AreaSaberAdmin)
admin.site.register(Curso, CursoAdmin)
admin.site.register(Disciplina, DisciplinaAdmin)

admin.site.register(Pessoa)
admin.site.register(Turma)
admin.site.register(Turno)
admin.site.register(Matricula)
admin.site.register(AvaliacaoTipo)
admin.site.register(Avaliacao)
admin.site.register(Frequencia)
admin.site.register(Ocorrencia)
admin.site.register(CursoDisciplina)