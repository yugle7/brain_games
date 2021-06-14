import comment.tests as comment
import discuss.tests as discuss
import person.tests as person
import poll.tests as poll
import puzzle.tests as puzzle
import solution.tests as solution


def data():
    person.Data()
    comment.Data()

    puzzle.Data()
    solution.Data()

    poll.Data()
    discuss.Data()
