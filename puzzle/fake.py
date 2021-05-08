from .models import *


class Fake(BaseFake):
    app = 'puzzle'

    categories = []
    puzzles = []
    comments = []

    def __init__(self):
        assert Person.objects.exists()

        Comment.objects.all().delete()
        Puzzle.objects.all().delete()
        Category.objects.all().delete()

        self.persons = Person.objects.all()
        self.create_categories()
        self.create_puzzles()
        self.create_comments()

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
                    puzzle=self.get_rand(self.puzzles),
                )
            )
