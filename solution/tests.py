from django.test import TestCase

from .models import *


class Data(BaseData):
    app = 'solution'

    solutions = []
    talks = []

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        assert Puzzle.objects.exists()
        self.puzzles = Puzzle.objects.all()

        assert Talk.objects.exists()
        self.talks = Talk.objects.all()

        Solution.objects.all().delete()

        self.create_solutions()
        self.create_talks()

    def create_solutions(self):
        for _ in range(10):
            self.solutions.append(
                Solution.objects.create(
                    puzzle=self.get_rand(self.puzzles),
                    author=self.get_rand(self.persons),
                    text=self.get_text(),
                    talk=self.get_rand(self.talks, 'solution')
                )
            )


class SolutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        solution = Solution.objects.first()
        self.assertEquals(solution.get_absolute_url(), f'/solution/{solution.id}/')
