from django.db import models
from datetime import datetime


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
    dataAlugou = models.DateField (verbose_name="Data do Aluguel", null=True)
    nomeAlugou = models.CharField(
        verbose_name="Nome do Locador", max_length=100, null=True
    )
    telefoneAlugou = models.IntegerField(
        verbose_name="Telefone do Locador", max_length=11, null=True
    )
    dataDevol = models.DateTimeField(null=True)

    class Meta:
        ordering = ["titulo"]

    def markTime(self):
        self.dataDevol = datetime.now()
        self.dataAlugou = None
        self.nomeAlugou = None
        self.telefoneAlugou = None
        self.save()