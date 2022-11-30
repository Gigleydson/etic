# Generated by Django 4.1.3 on 2022-11-30 18:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recibo_e_cautela', '0003_rename_observacoes_recibo_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='data',
            field=models.DateField(default=datetime.date(2022, 11, 30), verbose_name='Data'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='quantidade',
            field=models.CharField(max_length=100, verbose_name='Quantidade'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='ramal',
            field=models.CharField(max_length=4, verbose_name='Ramal'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='sinf',
            field=models.CharField(max_length=4, verbose_name='SINF'),
        ),
    ]