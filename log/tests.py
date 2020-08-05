from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from log.models import Log
from django.test import TestCase
from django.utils import timezone
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        Log.objects.create(text="LogText", date=timezone.now(),
                           time=timezone.now(), category='HP')

    def test_logs(self):
        log = Log.objects.all()
        self.assertEquals(log[0].text, "LogText")
        self.assertEquals(log[0].category, "HP")
        self.assertEquals(log[0].important, False)
        self.assertEquals(log[0].date, datetime.date.today())


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_logs = reverse('get_all_logs')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_logs)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_logs)
        self.assertEquals(response.status_code, 200)
        # self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        log = Log.objects.create(text="LogText", date=timezone.now(),
                                 time=timezone.now(), category='HP')
        log.save()
        response = self.client.get(self.get_all_logs)
        self.assertEquals(len(response.data), 1)
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'text', 'date', 'time',
                                                            'important', 'category')))
        self.assertEquals(response.data[0]["text"], "LogText")
