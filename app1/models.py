from django.db import models

Tipo_Despesa=(('1','Remedio'),('2','Alimentação'),('3','Educação'),('4','Transporte'))
Pagamento=(('1','Dinheiro'),('2','Cartão de Crédito'),('3','Cartão de Debito'))

class Despesa(models.Model):
    data_criacao= models.CharField("Data de criação", max_length=50)
    tipo_despesa= models.CharField("Tipo de despesa",max_length=50, choices=Tipo_Despesa)
    descricao= models.CharField("Descrição",max_length=40)
    forma_pag= models.CharField("Pagamento",max_length=30, choices=Pagamento)
    vencimento= models.DateField("Vencimento")
    quitado= models.BooleanField("Quitado")
