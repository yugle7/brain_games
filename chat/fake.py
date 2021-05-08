from utils import BaseFake
from .models import *


class Fake(BaseFake):
    app = 'chat'

    comments = []

    def __init__(self):
        Comment.objects.all().delete()
        self.persons = Person.objects.all()

        self.create_comments()

    def create_comments(self):
        for text in self.get_data('comments'):
            self.comments.append(
                Comment.objects.create(
                    text=text[0],
                    author=self.get_rand(self.persons),
                    person=self.get_rand(self.persons),
                    is_liked=self.get_coin()
                )
            )
