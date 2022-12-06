from django.db import models
import datetime


class Base(models.Model):
    criados = models.DateField('Criação', auto_now_add=True)
    modificado = models.DateField('Atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True


class Recibo(Base):
    nome = models.CharField('Nome', max_length=100)
    saram = models.CharField('Saram', max_length=7)
    graduacao = models.CharField('Posto / Graduação', max_length=100)
    setor = models.CharField('Setor / Seção', max_length=100)
    ramal = models.CharField('Ramal', max_length=4)
    data = models.DateField('Data', default=datetime.date.today())
    especificacoes = models.CharField('Especifiações', max_length=200)
    observacao = models.CharField('Observação', max_length=500)
    sinf = models.CharField('SINF', max_length=4)
    lacre = models.CharField('Lacre', max_length=7)
    bmp = models.CharField('BMP', max_length=10)
    quantidade = models.IntegerField('Quantidade', max_length=100)

    def __str__(self):
        return self.nome
