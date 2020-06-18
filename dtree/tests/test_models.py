from mixer.backend.django import mixer
import pytest
from dtree.models import Tree

@pytest.mark.django_db
class TestModels:


    def test_create_name(self):
        tree = Tree.objects.create(node="Node", tree="HUY")
        assert tree.tree == "HUY"