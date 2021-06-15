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
        answers = []
        for answer in self.get_data('answers'):
            answers.append(answer)

        reviews = []
        for review in self.get_data('reviews'):
            reviews.append(review)

        for answer in answers:
            params = {
                'author': self.get_rand(self.persons),
                'puzzle': self.get_rand(self.puzzles),
                'answer': answer,
            }

            while self.flip_coin():
                params['is_submitted'] = True
                if 'reviewer' not in params:
                    if self.flip_coin():
                        params['reviewer'] = self.get_rand(self.persons)
                    else:
                        break

                if self.flip_coin():
                    params['review'] = self.get_rand(reviews)

                    if self.flip_coin():
                        params['is_accepted'] = True
                        break

                    if self.flip_coin():
                        solution = Solution.objects.create(**params)
                        self.solutions.append(solution)

                        params = {
                            'author': params['author'],
                            'puzzle': params['puzzle'],
                            'reviewer': self.get_rand(self.persons),
                            'answer': self.get_rand(answers),
                        }

        solution = Solution.objects.create(**params)
        self.solutions.append(solution)


class SolutionTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Data()

    def test_get_absolute_url(self):
        solution = Solution.objects.first()
        self.assertEquals(solution.get_absolute_url(), f'/solution/{solution.id}/')
