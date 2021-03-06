# Generated by Django 2.2.7 on 2019-11-23 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Compra',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor')),
                ('data', models.DateField(verbose_name='Data')),
                ('cpf', models.CharField(max_length=11, verbose_name='CPF')),
                ('status', models.CharField(max_length=20, verbose_name='Status')),
                ('cashback_porcentagem', models.DecimalField(decimal_places=2, max_digits=2, verbose_name='Porcentagem de Cashback')),
                ('cashback_valor', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Valor do Cashback')),
            ],
        ),
        migrations.CreateModel(
            name='Revendedor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=80, verbose_name='Nome completo')),
                ('cpf', models.CharField(max_length=11, unique=True, verbose_name='CPF')),
                ('email', models.EmailField(max_length=120, unique=True, verbose_name='E-mail')),
                ('senha', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'revendedor',
                'verbose_name_plural': 'revendedores',
            },
        ),
    ]
