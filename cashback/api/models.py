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
    status = models.CharField('Status', max_length=20, default="Em validação")

    @property
    def cashback_porcentagem(self):
        if self.valor <= 1000:
            return 10
        elif self.valor > 1000 and self.valor <= 1500:
            return 15
        elif self.valor > 1500:
            return 20

    @property
    def cashback_valor(self):
        return round((self.cashback_porcentagem * self.valor) / 100, 2)

    def __str__(self):
        return f'{self.cpf} - {self.cashback_valor}'
