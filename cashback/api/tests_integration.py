from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework.test import APITestCase
from rest_framework import status

from decimal import Decimal

from api.models import Revendedor, Compra


class TestJWTAutenticacao(APITestCase):
    """
        Módulo de teste dos endpoints de JWT Autenticação.
    """
    def setUp(self):
        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

    def test_jwt_gerar_token(self):
        response = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TestLogin(APITestCase):
    """
        Módulo de teste do endpoint de Login do Revendedor.
    """
    def setUp(self):
        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

        self.token = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })

        Revendedor.objects.create(
            nome="Elis",
            email="elis@elis.com",
            cpf="12345678911",
            senha=make_password("123456")
        )

    def test_login_revendedor(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.post("/api/revendedores/login/", {
            "email": "elis@elis.com",
            "senha": "123456"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
class TestRevendedorCreate(APITestCase):
    """
        Módulo de teste dos endpoints do Revendedor.
    """
    def setUp(self):
        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

        self.token = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })
    
    def test_cadastrar_revendedor(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.post("/api/revendedores/", {
            "nome": "Elis",
            "cpf": "12345678911",
            "email": "elis@elis.com",
            "senha": "123456"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCompraListCreate(APITestCase):
    """
        Módulo de teste dos endpoints da Compra.
    """
    def setUp(self):
        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

        self.token = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })
    
    def test_listar_compras(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.get("/api/compras/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cadastrar_compras(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.post("/api/compras/", {
            "valor": 15.17,
            "data": "2019-11-29",
            "cpf": "12345678911"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_cadastrar_compra_para_cpf_15350946056(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.post("/api/compras/", {
            "valor": 49.99,
            "data": "2019-11-29",
            "cpf": "15350946056"
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCompraUpdateDelete(APITestCase):
    """
        Módulo de teste dos endpoints de Cashback.
    """
    def setUp(self):
        Compra.objects.create(
            valor=50.00,
            data="2019-11-29",
            cpf="12345678922"
        )

        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

        self.token = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })
    
    def test_atualizar_compras(self):
        compra = Compra.objects.get(cpf="12345678922")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.put("/api/compras/"+str(compra.id)+"/", {
            "valor": 227.30,
            "data": "2019-11-29",
            "cpf": "12345678922"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_remover_compras(self):
        compra = Compra.objects.get(cpf="12345678922")
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.delete("/api/compras/"+str(compra.id)+"/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestCashbackList(APITestCase):
    """
        Módulo de testes do acumulo de cashback
    """
    def setUp(self):
        Compra.objects.create(
            valor=50.00,
            data="2019-12-02",
            cpf="12345678933"
        )
        Compra.objects.create(
            valor=49.20,
            data="2019-12-02",
            cpf="12345678944"
        )
        Compra.objects.create(
            valor=102.87,
            data="2019-12-02",
            cpf="12345678955"
        )
        Compra.objects.create(
            valor=9.80,
            data="2019-12-02",
            cpf="12345678955"
        )

        self.user = User.objects.create(username="admin", email="admin@admin.com")
        self.user.set_password("123456")
        self.user.save()

        self.token = self.client.post("/api/token/", {
            "username": "admin",
            "password": "123456"
        })
    
    def test_list_total_cashback(self):
        self.client.credentials(HTTP_AUTHORIZATION="Bearer " + self.token.data['access'])
        response = self.client.get("/api/compras/cashback/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
