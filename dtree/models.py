from django.db import models

from mptt.models import MPTTModel, TreeForeignKey


class Tree(MPTTModel):
    tree = models.CharField(max_length=100)
    node = models.CharField(max_length=100)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', on_delete=models.CASCADE)

    def __str__(self):
        return "<Tree: {}, Node: {}>".format(self.tree, self.node)

    def __repr__(self):
        return self.__str__()
