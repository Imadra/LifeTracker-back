from django.db import models
# from django.utils.timezone import localtime
# local = localtime(new datetime())
from django.utils.translation import gettext_lazy as _
from datetime import datetime

# Create your models here.
class Log(models.Model):
    class Category(models.TextChoices):
        DISCOVERY = 'DS', _('DISCOVERY')
        DEPRESSIVE = 'DP', _('DEPRESSIVE')
        HAPPY = 'HP', _('HAPPY')
        OTHER = 'O', _('OTHER')

    text = models.TextField(max_length=2500, default="No text")
    date = models.DateField(auto_now=True)
    time = models.TimeField(auto_now=True)
    important = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)

    def __str__(self):
        return str(self.id)