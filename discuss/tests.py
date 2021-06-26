from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'discuss'

    topics = []
    discusses = []
    talks = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        assert Comment.objects.exists()
        self.comments = Comment.objects.all()

        Talk.objects.all().delete()
        Discuss.objects.all().delete()
        Topic.objects.all().delete()

        self.create_topics()
        self.create_discusses()
        self.create_talks()

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
                    topic=self.get_rand(self.topics),
                    author=self.get_rand(self.persons)
                )
            )

    def create_comments(self):
        for text in self.get_data('comments'):
            self.comments.append(
                Comment.objects.create(
                    text=text[0],
                    author=self.get_rand(self.persons),
                )
            )

    def create_talks(self):
        for comment in self.comments:
            self.talks.append(
                Talk.objects.create(
                    comment=comment,
                    discuss=self.get_rand(self.discusses)
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
