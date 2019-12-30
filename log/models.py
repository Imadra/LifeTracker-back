from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Log(models.Model):
    class Category(models.TextChoices):
    	DISCOVERY = 'DS', _('DISCOVERY')
    	DEPRESSIVE = 'DP', _('DEPRESSIVE')
    	HAPPY = 'HP', _('HAPPY')
    	OTHER = 'O', _('OTHER')

    text = models.TextField(max_length=500, default="No text")
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    important = models.BooleanField(default=False)
    category = models.CharField(max_length=20, choices=Category.choices, default=Category.OTHER)

    def __str__(self):
        return str(self.id)