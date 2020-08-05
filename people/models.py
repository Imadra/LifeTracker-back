from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField



# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=50, default="")
    age = models.IntegerField(default=0)
    commentary = models.CharField(max_length=100, default="")
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
    occupation = models.CharField(max_length=100, default="")
    field = models.CharField(max_length=100, default="")
    description = models.TextField(max_length=1000, default="")
    happiness = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
    img = models.CharField(max_length=50, default="")
    logo = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.id)
