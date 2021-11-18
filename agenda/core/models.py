from django.db import models

# Create your models here.
class Evento(models.Model):
    titulo= models.CharField(max_length=200)
    descricao= models.TextField(blank=True,null=True)
    data_evento= models.DateTimeField()
    data_criacao=models.DateTimeField(auto_now=True)


