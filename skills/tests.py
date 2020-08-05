from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from django.contrib.auth.models import User
import pytest
from skills.models import Skill
from django.test import TestCase
import datetime


@pytest.mark.django_db
class TestModels(TestCase):

    def setUp(self):
        Skill.objects.create(name="Skill")

    def test_logs(self):
        skill = Skill.objects.all()
        self.assertEquals(skill[0].name, "Skill")
        self.assertEquals(skill[0].field, "-")
        self.assertEquals(skill[0].importance, 0)
        self.assertEquals(skill[0].comprehense, 0)
        self.assertEquals(skill[0].commentary, "-")


class TestViews(APITestCase):

    def setUp(self):
        self.username = 'test'
        self.password = 'test'
        user = User.objects.create_user(self.username, self.username, self.password)
        user.save()
        self.user = user
        self.client = APIClient()
        self.get_all_skills = reverse('get_all_skills')

    def test_unauthorized(self):
        response = self.client.get(self.get_all_skills)
        self.assertEquals(response.status_code, 401)

    def test_main(self):
        self.client.force_authenticate(user=self.user)
        response = self.client.get(self.get_all_skills)
        self.assertEquals(response.status_code, 200)
        # self.assertIsInstance(response.data, list)
        self.assertEquals(len(response.data), 0)
        skill = Skill.objects.create(name="Skill")
        skill.save()
        response = self.client.get(self.get_all_skills)
        self.assertEquals(len(response.data), 1)
        # print(response.data[0])
        self.assertIsInstance(response.data[0], dict)
        self.assertTrue(all(k in response.data[0] for k in ('id', 'name', 'field', 'importance',
                                                            'comprehense', 'commentary')))
        self.assertEquals(response.data[0]["name"], "Skill")
