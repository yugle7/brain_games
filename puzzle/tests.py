from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'puzzle'

    categories = []
    puzzles = []
    comments = []
    talks = []

    def __init__(self):
        assert Person.objects.exists()

        Talk.objects.all().delete()
        Puzzle.objects.all().delete()
        Category.objects.all().delete()

        self.persons = Person.objects.all()
        self.create_categories()
        self.create_puzzles()
        self.create_comments()
        self.create_talks()

    def create_categories(self):
        for slug, name in self.get_data('categories'):
            self.categories.append(
                Category.objects.create(
                    slug=slug,
                    name=name
                )
            )

    def create_puzzles(self):
        for slug, title, text in self.get_data('puzzles'):
            self.puzzles.append(
                Puzzle.objects.create(
                    slug=slug,
                    title=title,
                    text=text,
                    author=self.get_rand(self.persons),
                    category=self.get_rand(self.categories),
                    weight=1
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
                    puzzle=self.get_rand(self.puzzles),
                    is_public=self.flip_coin()
                )
            )


class CategoryTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        category = Category.objects.first()
        self.assertEquals(category.get_absolute_url(), f'/puzzle/?category={category.slug}')


class PuzzleTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        puzzle = Puzzle.objects.first()
        self.assertEquals(puzzle.get_absolute_url(), f'/puzzle/{puzzle.slug}/')
