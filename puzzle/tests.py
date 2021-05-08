from django.test import TestCase

from person.tests import create_test_person
from .models import *


def create_test_category():
    return Category.objects.create(slug='category', name='Категория')


def create_test_puzzle():
    category = create_test_category()
    person = create_test_person()
    return Puzzle.objects.create(
        slug='puzzle',
        title='Задача',
        text='Описание',
        author=person,
        category=category
    )


class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_category()

    def test_get_absolute_url(self):
        category = Category.objects.first()
        self.assertEquals(category.get_absolute_url(), '/puzzle/?category=' + category.slug)


class PuzzleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_puzzle()

    def test_get_absolute_url(self):
        puzzle = Puzzle.objects.first()
        self.assertEquals(puzzle.get_absolute_url(), f'/puzzle/{puzzle.slug}/')
