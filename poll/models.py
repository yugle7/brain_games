from django.db import models

from const import *
from person.models import Person
from utils import *


class Poll(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN)

    title = models.CharField(max_length=MAX_TITLE_LEN, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Описание")
    search = models.TextField(blank=True, verbose_name="Поиск")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время правки")

    is_published = models.BooleanField(null=True, blank=True, verbose_name="Опубликована")
    is_multiple = models.BooleanField(default=False, verbose_name='Несколько вариантов')

    def __str__(self):
        return self.title

    def inc(self, votes):
        if len(votes) > 0:
            for vote in votes:
                vote.save()
        self.save()

    def dec(self, person):
        votes = person.vote_set(choice__poll=self)
        if votes.count() > 0:
            votes.delete()
        self.save()

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
        ordering = ['id']


class Choice(models.Model):
    name = models.CharField(max_length=MAX_TITLE_LEN, verbose_name="Название")
    votes = models.IntegerField(default=0, verbose_name='Голосов')

    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, verbose_name="Опрос")

    def inc(self):
        self.votes += 1
        self.save()

    def dec(self):
        self.votes -= 1
        self.save()

    def __str__(self):
        return f'{self.name} -> {self.poll}'

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'
        ordering = ['id']


class Vote(models.Model):
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE, verbose_name="Вариант")
    person = models.ForeignKey(Person, blank=True, on_delete=models.CASCADE, verbose_name="Пользователь")

    def __str__(self):
        return f'{self.person.username} -> {self.choice}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.choice.inc()
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.choice.dec()
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Голос'
        verbose_name_plural = 'Голоса'
        ordering = ['id']


