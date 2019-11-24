from rest_framework.decorators import (
    api_view, 
    permission_classes
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.hashers import (
    make_password, 
    check_password
)
from rest_framework.views import APIView

from api.models import Revendedor, Compra
from api.serializers import (
    RevendedorSerializer, 
    CompraSerializer
)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def revendedor_login(request):
    """
        Valida o login do Revendedor.
    """
    if request.data['email']:
        revendedor = Revendedor.objects.get(email=request.data['email'])
        senha_valida = check_password(request.data['senha'], revendedor.senha)
        if senha_valida:
            serializer = RevendedorSerializer(revendedor)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"senha": "a senha informada está incorreta"}, 
                status=status.HTTP_401_UNAUTHORIZED
            )
    return Response(
        {"email": "é necessário informar um e-mail válido"}, 
        status=status.HTTP_404_NOT_FOUND
    )


class RevendedorCreate(generics.CreateAPIView):
    """
        Cria um novo cadastro do Revendedor.
    """
    permission_classes = [IsAuthenticated]

    def post(self, request):
        self.serializer_class = RevendedorSerializer
        senha = request.data['senha']
        request.data['senha'] = make_password(senha)
        serializer = RevendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompraCreate(APIView):
    """
        Cria um novo cadastro de Compra.
    """
    permission_classes = [IsAuthenticated]

    def calc_porcentagem_cashback(self, valor):
        """
            Calcula o valor da porcentagem de Cashback.
        """
        if valor <= 1000:
            return 10
        elif valor > 1000 and valor <= 1500:
            return 15
        elif valor > 1500:
            return 20

    def calc_valor_cashback(self, valor, porcentagem):
        """
            Calcula o valor do Cashback.
        """
        valor_cashback = (porcentagem * valor) / 100
        return valor_cashback

    def post(self, request):
        porcentagem_cashback = self.calc_porcentagem_cashback(request.data['valor'])
        request.data['cashback_porcentagem'] = porcentagem_cashback

        valor_cashback = self.calc_valor_cashback(request.data['valor'], porcentagem_cashback)
        request.data['cashback_valor'] = valor_cashback

        if request.data['cpf'] == "15350946056":
            request.data['status'] = "Aprovado"

        self.serializer_class = CompraSerializer
        serializer = CompraSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
