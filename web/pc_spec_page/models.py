from django.db import models

# Create your models here.


class PcSpecs(models.Model):
    name = models.CharField(max_length=50)
    price = models.CharField(max_length=10)
    processor = models.CharField(max_length=50)
    memory = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'pc_specs'

    def __str__(self):
        return self.name
