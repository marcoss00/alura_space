from django.db import models
from django.utils import timezone


class Fotografia(models.Model):

    OPCOES_CATEGORIA = [
        ('NEBULOSA', 'Nebulosa'),
        ('ESTRELA', 'Estrela'),
        ('GALÁXIA', 'Galáxia'),
        ('PLANETA', 'Planeta'),
    ]

    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=100, choices=OPCOES_CATEGORIA, default='')
    descricao = models.TextField(null=False, blank=False)
    foto = models.ImageField(upload_to='fotos/%Y/%m/%d/', null=True, blank=True)
    publicada = models.BooleanField(default=False)
    # data_fotografia = models.DateTimeField(auto_now_add=True, blank=False)
    data_fotografia = models.DateTimeField(default=timezone.now, blank=False)

    def __str__(self):
        return self.nome