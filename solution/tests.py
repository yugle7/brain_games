from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'solution'

    reviews = []
    answers = []
    solutions = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        assert Puzzle.objects.exists()
        self.puzzles = Puzzle.objects.all()

        assert Talk.objects.exists()
        self.talks = Talk.objects.all()

        Review.objects.all().delete()
        Answer.objects.all().delete()
        Solution.objects.all().delete()

        self.create_solutions()
        self.create_answers()
        self.create_reviews()

    def create_solutions(self):
        for text in self.get_data('answers'):
            self.solutions.append(
                Solution.objects.create(
                    text=text[0],
                    author=self.get_rand(self.persons),
                    puzzle=self.get_rand(self.puzzles),
                    talk=self.get_rand(self.talks, 'solution')
                )
            )

    def create_answers(self):
        for solution in self.solutions:
            self.answers.append(
                Answer.objects.create(
                    solution=solution,
                    text=solution.text,
                )
            )

    def create_reviews(self):
        for text in self.get_data('reviews'):
            self.reviews.append(
                Review.objects.create(
                    text=text[0],
                    author=self.get_rand(self.persons),
                    answer=self.get_rand(self.answers)
                )
            )


class SolutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        solution = Solution.objects.first()
        self.assertEquals(solution.get_absolute_url(), f'/solution/{solution.id}/')
