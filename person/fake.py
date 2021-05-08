from django.contrib.auth.hashers import make_password

from person.models import *


def create_superuser(username='root'):
    Person.objects.create(
        username=username,
        email=username + '@bg.ru',
        password=make_password('123'),
        is_superuser=True,
        is_staff=True
    )


class Fake(BaseFake):
    app = 'person'

    roles = []
    persons = []
    comments = []

    def __init__(self):
        Person.objects.all().delete()
        Role.objects.all().delete()

        create_superuser()

        self.create_roles()
        self.create_persons()

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
