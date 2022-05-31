from django.db import models
from django.utils import timezone


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    def __str__(self):
        return self.nome


class Remedio(models.Model):
    nome = models.CharField(max_length=255)
    ean = models.CharField(max_length=255)
    marca = models.CharField(max_length=255)
    quantidade = models.CharField(max_length=255)
    principio_ativo = models.CharField(max_length=255)
    dosagem = models.CharField(max_length=255)
    descricao = models.TextField(max_length=255)
    data_criacao = models.DateTimeField(default=timezone.now)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.nome

