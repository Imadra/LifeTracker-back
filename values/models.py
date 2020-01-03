from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Value(models.Model):
	class Type(models.TextChoices):
		GOOD = 'G', _('GOOD')
		BAD = 'B', _('BAD')
	
	name = models.CharField(max_length=50, default="")
	importance = models.IntegerField(default=0, validators=[MaxValueValidator(100), MinValueValidator(0)])
	value_type = models.CharField(max_length=20, choices=Type.choices, default=Type.GOOD)

	def __str__(self):
		return str(self.id)