from django.db import models
from django.contrib.auth.models import User  # Importando o modelo User

class Aluno(models.Model):
    nome = models.CharField(max_length=100)
    status = models.CharField(max_length=10, choices=[('ativo', 'Ativo'), ('inativo', 'Inativo')])
    # Adicione outros campos que forem necessários.

    def __str__(self):
        return self.nome

class Orientador(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Relacionamento com o modelo User
    nome = models.CharField(max_length=100)
    # Adicione outros campos que forem necessários.

    def __str__(self):
        return self.nome

class Curso(models.Model):
    nome = models.CharField(max_length=100)
    # Adicione outros campos que forem necessários.

    def __str__(self):
        return self.nome
