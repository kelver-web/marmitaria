from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Pedido(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=50)
    proteinas = models.CharField(max_length=80)
    acompanhamentos = models.CharField(max_length=100)
    saladas = models.CharField(max_length=80)
    quantidade = models.CharField(max_length=20)
    email = models.EmailField(blank=True)
    telefone = models.CharField(max_length=20)
    endereco = models.CharField(max_length=80)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    observacao = models.TextField(blank=True, null=True)
    data = models.DateTimeField(auto_now=True)

    produtos = []

    class Meta:
        db_table = 'pedido'

    def __str__(self):
        return self.nome

    def soma_pedido(self):
        tot = int(self.quantidade) * int(self.valor)
        return (f'{tot:.2f}')
