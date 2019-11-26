from rest_framework import serializers

from api.models import Revendedor, Compra


class RevendedorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Revendedor
        fields = ('id', 'nome', 'cpf', 'email', 'senha')


class CompraSerializerInput(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('id', 'valor', 'data', 'cpf')


class CompraSerializerOutput(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = ('id', 'valor', 'data', 'cpf', 'status', 
            'cashback_porcentagem', 'cashback_valor')
