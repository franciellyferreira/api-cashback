from rest_framework import serializers

from api.models import Revendedor, Compra


class RevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revendedor
        fields = ('nome', 'cpf', 'email', 'senha')


class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('valor', 'data', 'cpf', 'status',
                  'cashback_porcentagem', 'cashback_valor')
