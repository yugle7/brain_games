import chat.fake as chat
import discuss.fake as discuss
import person.fake as person
import poll.fake as poll
import puzzle.fake as puzzle
import solution.fake as solution


def fake():
    person.Fake()
    puzzle.Fake()
    solution.Fake()
    discuss.Fake()
    poll.Fake()
    chat.Fake()
