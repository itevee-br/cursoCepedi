from django.urls import path, include

from . import views

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista/', views.lista_alunos, name='lista'),
    path('cadastrar/', views.cadastrar_aluno, name='cadastrar'),
]
