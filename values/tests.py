from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from values.models import Value
from django.test import TestCase
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        Value.objects.create(name="Value", user=user)

    def test_logs(self):
        value = Value.objects.all()
        self.assertEquals(value[0].name, "Value")
        self.assertEquals(value[0].importance, 0)
        self.assertEquals(value[0].value_type, "G")


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_values = reverse('get_all_values')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_values)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_values)
        self.assertEquals(response.status_code, 200)
        # self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        value = Value.objects.create(name="Value", user=self.user)
        value.save()
        response = self.client.get(self.get_all_values)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'name', 'importance', 'value_type')))
        self.assertEquals(response.data[0]["name"], "Value")
