from django.test import TestCase

from person.tests import create_test_person
from .models import *


def create_test_topic():
    return Topic.objects.create(slug='topic', title='Тема')


def create_test_discuss():
    person = create_test_person()
    topic = create_test_topic()
    return Discuss.objects.create(
        slug='discuss',
        title='Обсуждение',
        text='Описание',
        topic=topic,
        author=person
    )


class TopicTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_topic()

    def test_get_absolute_url(self):
        topic = Topic.objects.first()
        self.assertEquals(topic.get_absolute_url(), f'/discuss/?topic={topic.slug}')


class DiscussTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_discuss()

    def test_get_absolute_url(self):
        discuss = Discuss.objects.first()
        self.assertEquals(discuss.get_absolute_url(), f'/discuss/{discuss.slug}/')
