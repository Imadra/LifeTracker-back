from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    strength_list = ArrayField(
        models.CharField(max_length=50, default=""),
        blank=True,
        default=list
    )
    weakness_list = ArrayField(
        models.CharField(max_length=50, default=""),
        blank=True,
        default=list
    )
    habit_list = ArrayField(
        models.CharField(max_length=50, default=""),
        blank=True,
        default=list
    )
    description = models.TextField(max_length=1000, default="")
    happiness = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    img = models.CharField(max_length=50, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
