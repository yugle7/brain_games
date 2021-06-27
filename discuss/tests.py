from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'discuss'

    topics = []
    discusses = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        assert Comment.objects.exists()
        self.comments = Comment.objects.all()

        assert Talk.objects.exists()
        self.talks = Talk.objects.all()

        Discuss.objects.all().delete()
        Topic.objects.all().delete()

        self.create_topics()
        self.create_discusses()

    def create_topics(self):
        for slug, title in self.get_data('topics'):
            self.topics.append(
                Topic.objects.create(slug=slug, title=title)
            )

    def create_discusses(self):
        for slug, title in self.get_data('discusses'):
            self.discusses.append(
                Discuss.objects.create(
                    slug=slug,
                    title=title,
                    talk=self.get_rand(self.talks),
                    topic=self.get_rand(self.topics),
                    author=self.get_rand(self.persons)
                )
            )


class TopicTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        topic = Topic.objects.first()
        self.assertEquals(topic.get_absolute_url(), f'/discuss/?topic={topic.slug}')


class DiscussTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        discuss = Discuss.objects.first()
        self.assertEquals(discuss.get_absolute_url(), f'/discuss/{discuss.slug}/')
