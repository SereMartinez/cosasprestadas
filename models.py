from django.conf import settings
from django.db import models
from django.utils import timezone


class personas(models.Model):
    id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    dni = models.TextField()
    fecha_de_nacimiento = models.DateTimeField(auto_now_add=True)
    fecha_pedido = models.DateTimeField(
            blank=True, null=True)

    def objeto(self):
        self.nombre = id.now()
        self.save()

    def __str__(self):
        return self.title













































