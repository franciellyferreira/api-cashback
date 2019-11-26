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
from django.http import Http404

from api.models import Revendedor, Compra
from api.serializers import (
    RevendedorSerializer, 
    CompraSerializerInput,
    CompraSerializerOutput,
)


@api_view(['POST'])
# @permission_classes([IsAuthenticated])
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


class RevendedorCreate(APIView):
    """
        Cria um novo cadastro do Revendedor.
    """
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        senha = request.data['senha']
        request.data['senha'] = make_password(senha)
        serializer = RevendedorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompraListCreate(APIView):
    """
        Lista todas as compras cadastradas
        e cadastra uma nova compra.
    """
    # permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        compras = Compra.objects.all()
        serializer = CompraSerializerOutput(compras, many=True)
        return Response(serializer.data)

    def post(self, request):
        if request.data['cpf'] == "15350946056":
            request.data['status'] = "Aprovado"
        serializer = CompraSerializerInput(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CompraUpdateDelete(APIView):
    """
        Atualiza o cadastro de uma compra.
    """
    # permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return Compra.objects.get(pk=pk)
        except Compra.DoesNotExist:
            raise Http404

    def put(self, request, pk, format=None):
        compra = self.get_object(pk)
        if compra.status == "Em validação":
            self.serializer_class = CompraSerializerInput
            serializer = CompraSerializerInput(compra, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(
                {'status': 'Esta compra não pode ser editada.'},
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, pk, format=None):
        compra = self.get_object(pk)
        if compra.status == "Em validação":
            compra.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(
                {'status': 'Esta compra não pode ser deletada.'},
                status=status.HTTP_404_NOT_FOUND
            )
