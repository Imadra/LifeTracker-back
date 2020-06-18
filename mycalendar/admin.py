from django.contrib import admin

# Register your models here.
from .models import Day, Task

admin.site.register(Day)
admin.site.register(Task)