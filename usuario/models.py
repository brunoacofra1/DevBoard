from django.db import models

class UsuariosModel(models.Model):
    nome = models.CharField(max_length=50)
    login = models.EmailField(max_length=150)
    senha = models.TextField(max_length=64)
    