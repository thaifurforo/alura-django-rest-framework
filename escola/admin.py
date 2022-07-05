from django.contrib import admin
from escola.models import Aluno, Curso, Matricula

# Register your models here.
class AlunoAdmin(admin.ModelAdmin):
  list_display = ('id', 'nome', 'rg', 'cpf', 'data_nascimento')
  # Ao alterar um aluno, será possível clicar nos seguintes dados:
  list_display_links = ('id', 'nome')
  # Com base em quais dados podem ser realizadas pesquisas
  search_fields = ('nome', )
  # Quantos alunos irão ser exibidos por página
  list_per_page = 20

admin.site.register(Aluno, AlunoAdmin)

class CursoAdmin(admin.ModelAdmin):
  list_display = ('id', 'codigo_curso', 'descricao')
  list_display_links = ('id', 'codigo_curso')
  search_fields = ('codigo_curso', )

admin.site.register(Curso, CursoAdmin)

class MatriculaAdmin(admin.ModelAdmin):
  list_display = ('id', 'aluno', 'curso', 'periodo')
  list_display_links = ('id', )

admin.site.register(Matricula, MatriculaAdmin)