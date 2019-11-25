from django.db import models

# Create your models here.
class Estado(models.Model):
    name=models.CharField(max_length=100,primary_key=True)

    def __str__(self):
        return self.name

class Flor(models.Model):
    name=models.CharField(max_length=100, primary_key=True)
    valor=models.IntegerField()
    descripcion=models.IntegerField()
    estado=models.ForeignKey(Estado,on_delete=models.CASCADE)
    fotografia=models.ImageField(upload_to="florcitas",null=True)

    def __str__(self):
        return self.name