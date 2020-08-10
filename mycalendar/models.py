from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User


# Create your models here.

class Task(models.Model):
    name = models.CharField(max_length=100, default="")
    date = models.DateField(auto_now=True)
    done = models.BooleanField(default=False)
    finish_date = models.DateField(null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)

    def get_finish_year(self):
        return self.finish_date.year

    def get_finish_month(self):
        return self.finish_date.month

    def get_finish_day(self):
        return self.finish_date.day


class Day(models.Model):
    class Mood(models.TextChoices):
        NEUTRAL = 'N', _('NEUTRAL')
        DEPRESSIVE = 'D', _('DEPRESSIVE')
        HAPPY = 'H', _('HAPPY')

    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    note = models.CharField(max_length=500, default="")
    # thoughts = ArrayField(models.CharField(max_length=10, blank=True), null=True)
    mood = models.CharField(max_length=20, choices=Mood.choices, default=Mood.NEUTRAL)
    tasks = models.ManyToManyField(Task)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
