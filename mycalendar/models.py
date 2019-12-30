from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import gettext_lazy as _

# Create your models here.
class DayInfo(models.Model):
	class Mood(models.TextChoices):
		NEUTRAL = 'N', _('NEUTRAL')
		DEPRESSIVE = 'D', _('DEPRESSIVE')
		HAPPY = 'H', _('HAPPY')
	year = models.IntegerField(default=0)
	month = models.IntegerField(default=0)
	day = models.IntegerField(default=0)
	note = models.CharField(max_length=100, default="")
	# thoughts = ArrayField(models.CharField(max_length=10, blank=True), null=True)
	mood = models.CharField(max_length=20, choices=Mood.choices, default=Mood.NEUTRAL)
	# plans to implement

	def __str__(self):
		return str(self.id)