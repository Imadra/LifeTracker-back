from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from dtree.models import Tree
from django.test import TestCase


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        Tree.objects.create(node="Node", tree="Tree1", user=user)
        tree2 = Tree.objects.create(node="Root", tree="Tree2", user=user)
        Tree.objects.create(node="Child", tree="Tree2", parent=tree2, user=user)

    def test_tree1(self):
        tree1 = Tree.objects.get(tree="Tree1")
        self.assertEqual(tree1.tree, "Tree1")
        self.assertEqual(tree1.node, "Node")
        self.assertEqual(tree1.parent, None)

    def test_tree2(self):
        tree2 = Tree.objects.filter(tree="Tree2")
        self.assertEqual(len(tree2), 2)
        self.assertEqual(tree2[1].node, "Child")
        self.assertEqual(tree2[1].parent, tree2[0])


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_trees = reverse('get_all_trees')
        self.get_single_tree = reverse('get_tree')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_trees)
        self.assertEquals(response.status_code, 401)

    def test_tree(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_trees)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        tree = Tree.objects.create(tree="Tree", node="Node", user=self.user)
        tree.save()
        response = self.client.get(self.get_all_trees)
        self.assertEquals(len(response.data), 1)
        self.assertEquals(response.data[0], "Tree")
        # print(self.get_single_tree + "?tree=Tree")
        # response = self.client.get(self.get_single_tree + "get/Tree")
        # print(response)
        # self.assertIsInstance(response.data[0], dict)
        # self.assertTrue(all(k in response.data[0] for k in ('id', 'tree_id', 'children', 'attributes',
        #                                                     'name', 'parent_id', 'lft', 'rght', 'level', '_collapsed')))
        # self.assertEquals(response.data[0]["tree"], "Tree")