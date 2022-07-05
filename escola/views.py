from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializers import AlunoSerializer, CursoSerializer, ListaMatriculasAlunoSerializer, MatriculaSerializer, ListaAlunosMatriculadosEmUmCursoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class AlunosViewSet(viewsets.ModelViewSet):
  '''Exibindo todos os alunos e alunas'''
  queryset = Aluno.objects.all()
  serializer_class = AlunoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class CursosViewSet(viewsets.ModelViewSet):
  '''Exibindo todos os cursos'''
  queryset = Curso.objects.all()
  serializer_class = CursoSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class MatriculasViewSet(viewsets.ModelViewSet):
  '''Exibindo todas as matrículas'''
  queryset = Matricula.objects.all()
  serializer_class = MatriculaSerializer
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]


class ListaMatriculasAluno(generics.ListAPIView):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  'Listando cursos nos quais aluno está matriculado'
  def get_queryset(self):
    queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaMatriculasAlunoSerializer

class ListaAlunosMatriculados(generics.ListAPIView):
  authentication_classes = [BasicAuthentication]
  permission_classes = [IsAuthenticated]

  'Listando alunos e alunas matriculados em um curso'
  def get_queryset(self):
    queryset = Matricula.objects.filter(curso_id=self.kwargs['pk'])
    return queryset
  serializer_class = ListaAlunosMatriculadosEmUmCursoSerializer
