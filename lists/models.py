from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


# Create your models here.
class List(models.Model):
    name = models.CharField(max_length=50, default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    entries = ArrayField(
        models.CharField(max_length=50, default=""),
        blank=True,
        default=list
    )

    def __str__(self):
        return str(self.id)


class Entry(models.Model):
    name = models.CharField(max_length=50, default="")
    list = models.ForeignKey(List, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return str(self.id)
