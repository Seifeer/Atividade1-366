from django.db import models

class Curso(models.Model):
    nome_curso=models.CharField("Curso",max_length=50)
    carga_h=models.IntegerField("Carga Horária")
    ementa=models.CharField("Ementa",max_length=40)
    Valor=models.FloatField("Valor")

class Turma(models.Model):
    #curso=models.ForeignKey(Curso,on_delete=models.CASCADE)
    data_i=models.DateField("Data de Inicio")
    data_t=models.DateField("Data de Término")
    hora_i=models.TimeField("Hora de Inicio")
    hora_t=models.TimeField("Hora de Termino")

class Professor(models.Model):
    nome=models.CharField("Nome",max_length=50)
    telefone=models.CharField("Telefone",max_length=20)
    valor_hora_aula=models.FloatField("Valor da Aula por Hora")