from django.test import TestCase

from person.models import *


def create_test_person():
    role = Role.objects.create(slug='role', name='Роль')
    return Person.objects.create(
        username='username',
        email='email@bg.ru',
        password='password',
        role=role
    )


def create_test_role():
    return Role.objects.create(slug='role', name='Роль')


class RoleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_role()

    def test_get_absolute_url(self):
        role = Role.objects.first()
        self.assertEquals(role.get_absolute_url(), '/person/?role=' + role.slug)


class PersonTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_person()

    def test_get_absolute_url(self):
        person = Person.objects.first()
        self.assertEquals(person.get_absolute_url(), f'/person/{person.username}/')
