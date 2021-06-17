
from django.db import models
from django.urls import reverse

from comment.models import Comment
from const import *
from person.models import Person
from poll.models import Poll
from utils import *


class Topic(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)

    title = models.CharField(max_length=MAX_TITLE_LEN, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Описание")

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'{reverse("discuss-list")}?topic={self.slug}'

    class Meta:
        verbose_name = 'Тема'
        verbose_name_plural = 'Темы'
        ordering = ['id']


class Discuss(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)

    title = models.CharField(max_length=MAX_TITLE_LEN, verbose_name="Название")
    text = models.TextField(blank=True, verbose_name="Описание")
    search = models.TextField(blank=True, verbose_name="Поиск")

    topic = models.ForeignKey(Topic, on_delete=models.PROTECT, verbose_name="Тема")
    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    poll = models.OneToOneField(Poll, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Опрос')

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def save(self, *args, **kwargs):
        self.search = get_search(self.title + ' ' + self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discuss-detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        ordering = ['-update_time']


class Talk(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.PROTECT, related_name='discuss_talk', verbose_name="Комментарий"
    )
    discuss = models.ForeignKey(Discuss, on_delete=models.PROTECT, verbose_name="Обсуждение")

    def __str__(self):
        return f'{self.comment.author} -> {self.discuss}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
