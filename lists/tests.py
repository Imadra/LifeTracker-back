from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from lists.models import List
from django.test import TestCase
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        List.objects.create(name="List", user=user)

    def test_logs(self):
        value = List.objects.all()
        self.assertEquals(value[0].name, "List")


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_lists = reverse('get_all_lists')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_lists)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_lists)
        self.assertEquals(response.status_code, 200)
        # self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        value = List.objects.create(name="List", user=self.user)
        value.save()
        response = self.client.get(self.get_all_lists)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'name')))
        self.assertEquals(response.data[0]["name"], "List")
