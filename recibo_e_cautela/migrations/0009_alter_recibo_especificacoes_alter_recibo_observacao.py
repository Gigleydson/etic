# Generated by Django 4.1.3 on 2022-12-06 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recibo_e_cautela', '0008_alter_recibo_data_alter_recibo_observacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recibo',
            name='especificacoes',
            field=models.CharField(max_length=300, verbose_name='Especifiações'),
        ),
        migrations.AlterField(
            model_name='recibo',
            name='observacao',
            field=models.CharField(max_length=300, verbose_name='Observação'),
        ),
    ]
