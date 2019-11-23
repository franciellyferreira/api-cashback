from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics
from django.contrib.auth.hashers import (
    make_password, 
    check_password
)

from api.models import Revendedor
from api.serializers import RevendedorSerializer


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
