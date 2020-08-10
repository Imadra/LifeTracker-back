from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User


# Create your models here.
class Skill(models.Model):
    name = models.CharField(max_length=50, default="-")
    field = models.CharField(max_length=50, default="-")
    importance = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    comprehense = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    commentary = models.CharField(max_length=100, default="-")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
