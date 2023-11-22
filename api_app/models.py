from django.db import models

# Create your models here.


class MiniatureSize(models.Model):
    height = models.PositiveIntegerField()
    width = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.height}x{self.width}'
