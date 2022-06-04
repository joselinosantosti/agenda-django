from django.db import models
from django.utils import timezone

class Departamento(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome

class Empregado(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    aniversario = models.DateField()
    descricao = models.TextField(blank=True)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m/%d/')

    def __str__(self):
        return self.nome
