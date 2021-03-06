from django.test import TestCase

from utils import BaseData
from .models import *


class Data(BaseData):
    app = 'comment'

    talks = []
    comments = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        Talk.objects.all().delete()
        self.create_talks()

        Comment.objects.all().delete()
        self.create_comments()

    def create_talks(self):
        for i in range(20):
            self.talks.append(
                Talk.objects.create()
            )

    def create_comments(self):
        for _ in range(100):
            self.comments.append(
                Comment.objects.create(
                    text=self.get_text(),
                    author=self.get_rand(self.persons),
                    talk=self.get_rand(self.talks),
                )
            )


class TopicTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()
