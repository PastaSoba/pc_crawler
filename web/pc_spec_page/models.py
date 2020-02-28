from django.db import models

# Create your models here.


class PC_SPEC(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)

    def __str__(self):
        return self.name
