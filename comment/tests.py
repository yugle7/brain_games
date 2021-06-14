from django.test import TestCase

from utils import BaseData
from .models import *


class Data(BaseData):
    app = 'comment'

    comments = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        Comment.objects.all().delete()
        self.create_comments()

    def create_comments(self):
        for text in self.get_data('comments'):
            comment = Comment.objects.create(
                text=text[0],
                author=self.get_rand(self.persons),
            )
            self.comments.append(comment)


class TopicTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()