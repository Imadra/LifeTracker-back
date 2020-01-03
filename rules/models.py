from django.db import models

from mptt.models import MPTTModel, TreeForeignKey

class RuleTree(MPTTModel):
   name = models.CharField(max_length=100)
   # attributes = models.CharField(max_length=100)
   parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

   def __str__(self):
       return "<RuleTree: {}>".format(self.name)

   def __repr__(self):
       return self.__str__()