from django.db import models

# Create your models here.
class DayInfo(models.Model):
    year = models.IntegerField(default=0)
    month = models.IntegerField(default=0)
    day = models.IntegerField(default=0)
    info = models.CharField(max_length=100, default="Codeforces black")

    def __str__(self):
        return str(self.id)