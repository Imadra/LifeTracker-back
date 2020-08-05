from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from mycalendar.models import Task, Day
from django.test import TestCase
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        Task.objects.create(name="Task")

    def test_logs(self):
        task = Task.objects.all()
        self.assertEquals(task[0].name, "Task")
        self.assertEquals(task[0].done, False)
        self.assertEquals(task[0].finish_date, None)


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_tasks = reverse('get_all_tasks')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_tasks)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_tasks)
        self.assertEquals(response.status_code, 200)
        self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        task = Task.objects.create(name="Task")
        task.save()
        response = self.client.get(self.get_all_tasks)
        self.assertEquals(len(response.data), 1)
        # print(response.data[0])
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'name', 'date', 'done')))
        self.assertEquals(response.data[0]["name"], "Task")
