from django.db import models

class Nota(models.Model):
    titulo = models.CharField(max_length=200)
    contenido = models.CharField(max_length=1000)
    fecha = models.TimeField()

    def __str__(self) -> str:
        return self.titulo
