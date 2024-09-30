from django.db import models


class livros(models.Model):
    titulo = models.CharField(
        verbose_name="Título", max_length=100, null=False, blank=False
    )
    autor = models.CharField(
        verbose_name="Autor", max_length=100, null=False, blank=False
    )
    genero = models.CharField(
        verbose_name="Gênero", max_length=100, null=False, blank=False
    )
    anoPublicacao = models.DateField(
        verbose_name="Ano de Publicação", null=False, blank=False
    )
    dataAlugou = models.DateTimeField(null=True)
    nomeAlugou = models.CharField(max_length=100, null=True)
    telefoneAlugou = models.IntegerField(max_length=11, null=True)
    dataDevol = models.DateTimeField(null=True)
