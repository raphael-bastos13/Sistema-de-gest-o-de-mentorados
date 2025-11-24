from django.db import models
from django.contrib.auth.models import User

class Navigators(models.Model):
    nome = models.CharField(max_length=255)
    user = models.ForeignKey(User,on_delete=models.CASCADE) 

    def __str__(self):
        return self.nome

# Create your models here.
class Mentorados(models.Model):
    estagio_choices = (
        ('E1', '10-100k'),
        ('E2', '100-500k'),
        ('E3', '500k-1M'),
        ('E4', '1M+'),
    )
    nome = models.CharField(max_length=255) # Nome do mentorado
    criado_em = models.DateField(auto_now_add=True) # Data de criação do registro 
    foto = models.ImageField(upload_to='fotos', null=True, blank=True) # Foto do mentorado
    estagio = models.CharField(max_length=2,  choices=estagio_choices) # Estágio do mentorado
    navigator = models.ForeignKey(Navigators, null=True, blank=True, on_delete=models.CASCADE) # Navigator associado ao mentorado
    user = models.ForeignKey(User,on_delete=models.CASCADE) # Usuário associado ao mentorado

    def __str__(self):
        return self.nome
