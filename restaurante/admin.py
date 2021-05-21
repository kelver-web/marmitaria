from django.contrib import admin
from restaurante.models import Pedido

# Register your models here.


class PedidoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'proteinas', 'acompanhamentos', 'saladas',
                    'quantidade', 'email', 'telefone', 'endereco',
                    'valor', 'observacao', 'data')
    list_filter = ('usuario', 'nome', 'data',)
    ordering = ('usuario',)


admin.site.register(Pedido, PedidoAdmin)
