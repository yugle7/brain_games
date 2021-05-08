from .models import *


class Fake(BaseFake):
    app = 'discuss'

    topics = []
    discusses = []
    comments = []
    reactions = []

    def __init__(self):
        assert Person.objects.exists()

        Reaction.objects.all().delete()
        Comment.objects.all().delete()
        Discuss.objects.all().delete()
        Topic.objects.all().delete()

        self.persons = Person.objects.all()
        self.create_topics()
        self.create_discusses()
        self.create_comments()
        self.create_reactions()

    def create_topics(self):
        for slug, title in self.get_data('topics'):
            self.topics.append(
                Topic.objects.create(slug=slug, title=title)
            )

    def create_discusses(self):
        for slug, title in self.get_data('discusses'):
            self.discusses.append(
                Discuss.objects.create(
                    slug=slug,
                    title=title,
                    topic=self.get_rand(self.topics),
                    author=self.get_rand(self.persons)
                )
            )

    def create_comments(self):
        for text in self.get_data('comments'):
            discuss = self.get_rand(self.discusses)
            replies = Comment.objects.filter(discuss=discuss)

            answer = Comment.objects.create(
                text=text[0],
                author=self.get_rand(self.persons),
                discuss=discuss
            )
            if len(replies) > 0 and self.get_coin():
                answer.reply = self.get_rand(replies)
                answer.save()

            self.comments.append(answer)

    def create_reactions(self):
        for person in self.persons:
            comment = self.get_rand(self.comments)
            self.reactions.append(
                Reaction.objects.create(
                    comment=comment,
                    person=person,
                    is_liked=self.get_coin()
                )
            )
