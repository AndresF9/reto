from django.db import models

class Cliente(models.Model):
    Identificacion=models.CharField(max_length=20)
    Nombre=models.CharField(max_length=30)
    Telefono=models.CharField(max_length=20)
    Correo=models.EmailField()
    Departamento=models.CharField(max_length=20)
    Ciudad=models.CharField(max_length=20)
    Edad=models.IntegerField()

class Evento(models.Model):
    Fecha=models.DateField()
    Personas=models.IntegerField()
    Observaciones=models.TextField()
    Estado=models.CharField(max_length=20,choices=[('No Confirmado','No Confirmado'),('Confirmado','Confirmado')], default="No confirmado")

    MOTIVO_CHOICES = [
        ('evento_empresarial', 'Evento empresarial'),
        ('despedida_empresa', 'Despedida de la empresa'),
        ('desayuno_comercial', 'Desayuno comercial'),
        ('almuerzo', 'Almuerzo'),
    ]

    motivo = models.CharField(
        max_length=20,
        choices=MOTIVO_CHOICES,
        default='evento_empresarial'
    )
    Cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
# Create your models here.
