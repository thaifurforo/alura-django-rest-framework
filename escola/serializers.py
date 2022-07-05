from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula

class AlunoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Aluno
    fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento']

class CursoSerializer(serializers.ModelSerializer):
  class Meta:
    model = Curso
    fields = '__all__'

class MatriculaSerializer(serializers.ModelSerializer):
  class Meta:
    model = Matricula
    # Equivalente a fields = "__all__" se deixar o exclude vazio. Se não pode colocar dentro do exclude só os fields que não quer puxar pro serializer
    exclude = []

class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
  # Para pegar a descrição na exibição do objeto curso, e não o id:
  curso = serializers.ReadOnlyField(source='curso.descricao')

  # Como o período é um ChoiceField, dessa forma busca o correspondente de exibição dele no GET:
  periodo = serializers.SerializerMethodField()
  def get_periodo(self, obj):
    return obj.get_periodo_display()
  
  class Meta:
    model = Matricula
    fields = ['curso', 'periodo']
  
class ListaAlunosMatriculadosEmUmCursoSerializer(serializers.ModelSerializer):
  aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
  class Meta:
    model = Matricula
    fields = ['aluno_nome']