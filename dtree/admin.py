from django.contrib import admin
from .models import CodeforcesTree, RuleTree, EconTree

# Register your models here.
admin.site.register(CodeforcesTree)
admin.site.register(RuleTree)
admin.site.register(EconTree)