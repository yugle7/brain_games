from django.test import TestCase

from puzzle.tests import create_test_puzzle
from .models import *


def create_test_solution():
    create_test_puzzle()
    return Solution.objects.create(
        draft='Черновик',
        puzzle=Puzzle.objects.first(),
        author=Person.objects.first()
    )


class SolutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        create_test_solution()

    def test_get_absolute_url(self):
        solution = Solution.objects.first()
        self.assertEquals(solution.get_absolute_url(), f'/solution/{solution.id}/')
