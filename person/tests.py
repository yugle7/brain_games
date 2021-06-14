from django.contrib.auth.hashers import make_password
from django.test import TestCase

from comment.models import Comment
from person.models import *


def create_superuser(username='root'):
    Person.objects.create(
        username=username,
        email=username + '@bg.ru',
        password=make_password('123'),
        is_superuser=True,
        is_staff=True
    )


class Data(BaseData):
    app = 'person'

    roles = []
    persons = []
    talks = []

    def __init__(self):
        Person.objects.all().delete()
        Role.objects.all().delete()

        create_superuser()

        self.create_roles()
        self.create_persons()
        self.create_talks()

    def create_roles(self):
        for slug, name in self.get_data('roles'):
            self.roles.append(
                Role.objects.create(slug=slug, name=name)
            )

    def create_persons(self):
        for username, about in self.get_data('persons'):
            self.persons.append(
                Person.objects.create(
                    username=username,
                    about=about,
                    email=username + '@bg.ru',
                    password=make_password('123'),
                    role=self.get_rand(self.roles)
                )
            )

    def create_talks(self):
        for text in self.get_data('comments'):
            comment = Comment.objects.create(
                text=text[0],
                author=self.get_rand(self.persons),
            )
            self.talks.append(
                Talk.objects.create(
                    comment=comment,
                    person=self.get_rand(self.persons)
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
