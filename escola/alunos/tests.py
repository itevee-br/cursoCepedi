from django.test import TestCase
from .models import Aluno
from django.urls import reverse
from django.contrib.auth.models import User

class AlunoModelTest(TestCase):

    def test_criar_aluno(self):
        aluno = Aluno.objects.create(
            nome="Teste",
            idade=20,
            email="teste@email.com"
        )

        self.assertEqual(aluno.nome, "Teste")
        self.assertEqual(aluno.idade, 20)

        self.assertTrue(aluno.matriculado)


class AlunoViewTest(TestCase):
    def setUp(self):
            self.user = User.objects.create_user(
                username="teste",
                password="teste"
            )
            self.client.login(username="teste", password="teste")
    def test_lista_alunos_status(self):
        response = self.client.get('/alunos/cadastrar/')
        self.assertEqual(response.status_code, 200)
