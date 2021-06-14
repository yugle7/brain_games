from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'solution'

    solutions = []

    def __init__(self):
        assert Person.objects.exists()
        assert Puzzle.objects.exists()

        Solution.objects.all().delete()

        self.persons = Person.objects.all()
        self.puzzles = Puzzle.objects.all()
        self.create_solutions()

    def create_solutions(self):
        texts = []
        reviews = []
        for text, review in self.get_data('solutions'):
            texts.append(text)
            reviews.append(review)
        for draft in texts:
            solution = Solution.objects.create(
                draft=draft,
                author=self.get_rand(self.persons),
                puzzle=self.get_rand(self.puzzles)
            )
            if self.get_coin():
                solution.to_submit()
                if self.get_coin():
                    solution.reviewer = self.get_rand(self.persons)
                    if self.get_coin():
                        solution.review = self.get_rand(reviews)
                        if self.get_coin():
                            solution.to_accept()
                        elif self.get_coin():
                            solution.draft = self.get_rand(texts)
                            solution.to_submit()
                solution.save()

            self.solutions.append(solution)


class SolutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        solution = Solution.objects.first()
        self.assertEquals(solution.get_absolute_url(), f'/solution/{solution.id}/')
