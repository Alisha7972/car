from django.db import models

class Car(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100)
    year = models.IntegerField()

    def __str__(self):
        return f"{self.brand} {self.name} ({self.year})"



# Create your models here.
