from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework import status
from decimal import Decimal

from api.models import Revendedor, Compra


class RevendedorTest(TestCase):
    """
        Módulo de teste da model Revendedor.
    """
    def setUp(self):
        Revendedor.objects.create(
            nome="Elis", 
            email="elis@elis.com", 
            cpf="12345678911", 
            senha="top_secret_elis"
        )
        Revendedor.objects.create(
            nome="Rafael", 
            email="rafael@rafael.com", 
            cpf="12345678922", 
            senha="top_secret_rafael"
        )

    def test_revendedor_name(self):
        revendedor = Revendedor.objects.get(nome="Elis")
        self.assertEqual(revendedor.email, "elis@elis.com")

    def test_revendedor_email(self):
        revendedor = Revendedor.objects.get(email="rafael@rafael.com")
        self.assertEqual(revendedor.nome, "Rafael")
    
    def test_revendedor_cpf(self):
        revendedor = Revendedor.objects.get(cpf="12345678911")
        self.assertEqual(revendedor.email, "elis@elis.com")

    def test_revendedor_senha(self):
        revendedor = Revendedor.objects.get(
            email="rafael@rafael.com", 
            senha="top_secret_rafael"
        )
        self.assertEqual(revendedor.nome, "Rafael")


class CompraTest(TestCase):
    """
        Módulo de teste da model Compra.
    """
    def setUp(self):
        Compra.objects.create(
            valor=237.40,
            data="2019-11-26",
            cpf="12345678911"
        )

    def test_compra_cashback_porcentagem(self):
        compra = Compra.objects.get(cpf="12345678911")
        self.assertEqual(compra.cashback_porcentagem, 10)

    def test_compra_cashback_valor(self):
        compra = Compra.objects.get(cpf="12345678911")
        self.assertEqual(compra.cashback_valor, Decimal(str(23.74)))
