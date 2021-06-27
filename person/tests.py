from django.contrib.auth.hashers import make_password
from django.test import TestCase

from person.models import *


def create_superuser(username='root'):
    Person.objects.create(
        username=username,
        email=username + '@bg.ru',
        password=make_password('bg'),
        is_superuser=True,
        is_staff=True
    )


class Data(BaseData):
    app = 'person'

    roles = []
    persons = []

    def __init__(self):
        Person.objects.all().delete()
        Role.objects.all().delete()

        create_superuser()

        self.create_roles()
        self.create_persons()

    def create_roles(self):
        for slug, name in self.get_roles():
            self.roles.append(
                Role.objects.create(slug=slug, name=name)
            )

    def create_persons(self):
        for _ in range(20):
            username = self.get_username()
            self.persons.append(
                Person.objects.create(
                    username=username,
                    about=self.get_text(),
                    email=username + '@bg.ru',
                    password=make_password('bg'),
                    role=self.get_rand(self.roles)
                )
            )


class RoleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        role = Role.objects.first()
        self.assertEquals(role.get_absolute_url(), f'/person/?role={role.slug}')


class PersonTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        person = Person.objects.first()
        self.assertEquals(person.get_absolute_url(), f'/person/{person.username}/')
