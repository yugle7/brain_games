from .models import *


class Data(BaseData):
    app = 'poll'

    def __init__(self):
        assert Person.objects.exists()
        self.persons = Person.objects.all()

        Poll.objects.all().delete()
        Vote.objects.all().delete()
        Choice.objects.all().delete()

        self.polls = self.create_polls()
        self.choices = self.create_choices()
        self.vote = self.create_votes()

    def create_polls(self):
        polls = []
        for slug, title in self.get_data('polls'):
            polls.append(
                Poll.objects.create(
                    slug=slug,
                    title=title,
                    author=self.get_rand(self.persons),
                    is_multiple=self.flip_coin()
                )
            )
        return polls

    def create_choices(self):
        choices = []

        for name in self.get_data('choices'):
            choices.append(
                Choice.objects.create(
                    name=name[0],
                    poll=self.get_rand(self.polls),
                )
            )
        return choices

    def create_votes(self):
        votes = []

        for person in self.persons:
            for poll in self.polls:
                if self.flip_coin():
                    choices = poll.choice_set.all()
                    vote = Vote(
                        choice=self.get_rand(choices),
                        person=person,
                    )
                    votes = [vote]
                    if poll.is_multiple:
                        choice = self.get_rand(choices)
                        if choice.id != vote.choice.id:
                            votes.append(
                                Vote(
                                    choice=choice,
                                    person=person,
                                )
                            )
                    poll.inc(votes)
            votes.append(vote)

        return votes
