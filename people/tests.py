from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from people.models import Person
from django.test import TestCase
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        Person.objects.create(name="Chandler")

    def test_logs(self):
        person = Person.objects.all()
        self.assertEquals(len(person), 1)
        self.assertEquals(person[0].name, "Chandler")
        self.assertEquals(person[0].age, 0)
        self.assertEquals(person[0].commentary, "")
        self.assertEquals(person[0].strength_list, [])
        self.assertEquals(person[0].weakness_list, [])
        self.assertEquals(person[0].habit_list, [])
        self.assertEquals(person[0].occupation, "")
        self.assertEquals(person[0].field, "")
        self.assertEquals(person[0].description, "")
        self.assertEquals(person[0].happiness, 0)
        self.assertEquals(person[0].img, "")
        self.assertEquals(person[0].logo, "")


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_persons = reverse('get_all_persons')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_persons)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_persons)
        self.assertEquals(response.status_code, 200)
        # self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        person = Person.objects.create(name="Chandler")
        person.save()
        response = self.client.get(self.get_all_persons)
        self.assertEquals(len(response.data), 1)
        # print(response.data[0])
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ['id', 'name', 'age', 'commentary',
                                                            'strength_list', 'weakness_list', 'habit_list',
                                                            'occupation', 'field', 'description',
                                                            'happiness', 'img', 'logo']))
        self.assertEquals(response.data[0]["name"], "Chandler")
