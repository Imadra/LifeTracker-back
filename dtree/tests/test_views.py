from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from dtree.models import CodeforcesTree, RuleTree, EconTree
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
import json

class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_codeforces_url = reverse('get_codeforces_tree')
        self.get_econ_url = reverse('get_econ_tree')
        self.get_rules_url = reverse('get_rules_tree')

    def test_unauthorized(self):
        response = self.client.get(self.get_codeforces_url)
        self.assertEquals(response.status_code, 401)
        response = self.client.get(self.get_econ_url)
        self.assertEquals(response.status_code, 401)
        response = self.client.get(self.get_rules_url)
        self.assertEquals(response.status_code, 401)

    def test_codeforces_tree(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_codeforces_url)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        ctree = CodeforcesTree.objects.create()
        ctree.name = "Root"
        ctree.save()
        response = self.client.get(self.get_codeforces_url)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'tree_id', 'children', 'attributes',
                                                            'name', 'parent_id', 'lft', 'rght', 'level', '_collapsed')))
        self.assertEquals(response.data[0]["name"], "Root")

    def test_econ_tree(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_econ_url)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        etree = EconTree.objects.create()
        etree.name = "Root"
        etree.save()
        response = self.client.get(self.get_econ_url)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'tree_id', 'children', 'attributes',
                                                            'name', 'parent_id', 'lft', 'rght', 'level', '_collapsed')))
        self.assertEquals(response.data[0]["name"], "Root")

    def test_rules_tree(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_rules_url)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        rtree = RuleTree.objects.create()
        rtree.name = "Root"
        rtree.save()
        response = self.client.get(self.get_rules_url)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'tree_id', 'children', 'attributes',
                                                            'name', 'parent_id', 'lft', 'rght', 'level', '_collapsed')))
        self.assertEquals(response.data[0]["name"], "Root")