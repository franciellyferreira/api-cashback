from django.db import models


class Revendedor(models.Model):
    nome = models.CharField('Nome completo', max_length=80)
    cpf = models.CharField('CPF', max_length=11, unique=True)
    email = models.EmailField('E-mail', max_length=120, unique=True)
    senha = models.CharField(max_length=100)

    class Meta:
        verbose_name = ('revendedor')
        verbose_name_plural = ('revendedores')


class Compra(models.Model):
    valor = models.DecimalField('Valor', max_digits=8, decimal_places=2)
    data = models.DateField('Data')
    cpf = models.CharField('CPF', max_length=11)
    status = models.CharField('Status', max_length=20)
    cashback_porcentagem = models.DecimalField(
        'Porcentagem de Cashback',
        max_digits=2,
        decimal_places=2
    )
    cashback_valor = models.DecimalField(
        'Valor do Cashback',
        max_digits=8,
        decimal_places=2
    )

    def __str__(self):
        return f'{self.cpf} - {self.cashback_valor}'
