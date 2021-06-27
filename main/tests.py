import comment.tests as comment
import discuss.tests as discuss
import person.tests as person
import poll.tests as poll
import puzzle.tests as puzzle
import solution.tests as solution

from comment.models import Talk, Comment
from discuss.models import Discuss, Topic
from person.models import Person, Role
from poll.models import Poll, Vote, Choice
from puzzle.models import Puzzle, Category
from solution.models import Solution, Review, Answer


def data():
    Comment.objects.all().delete()
    Talk.objects.all().delete()

    Vote.objects.all().delete()
    Choice.objects.all().delete()
    Poll.objects.all().delete()

    Discuss.objects.all().delete()
    Topic.objects.all().delete()

    Review.objects.all().delete()
    Answer.objects.all().delete()
    Solution.objects.all().delete()

    Puzzle.objects.all().delete()
    Category.objects.all().delete()

    Person.objects.all().delete()
    Role.objects.all().delete()

    person.Data()
    comment.Data()

    puzzle.Data()
    solution.Data()

    poll.Data()
    discuss.Data()
