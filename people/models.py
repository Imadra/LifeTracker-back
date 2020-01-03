from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=50, default="")
    commentary = models.CharField(max_length=100, default="")
    strengths = models.CharField(max_length=100, default="")
    weaknesses = models.CharField(max_length=100, default="")
    happyness = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    img = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.id)