from django.db import models

class box(models.Model):
    nome = models.CharField(max_length=100)
    numero = models.IntegerField()
    def __str__(self):
     return self.nome
