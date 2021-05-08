from django.db import models
from django.urls import reverse

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
        return f'{reverse("discuss_list")}?topic={self.slug}'

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

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время изменения")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время правки")

    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    comments_count = models.IntegerField(default=0, verbose_name='Комментариев')
    persons_count = models.IntegerField(default=0, verbose_name='Участников')

    poll = models.OneToOneField(Poll, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Опрос')

    def save(self, *args, **kwargs):
        self.search = get_search(self.title + ' ' + self.text)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_discuss', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Обсуждение'
        verbose_name_plural = 'Обсуждения'
        ordering = ['-update_time']


class Comment(models.Model):
    text = models.TextField(blank=True, verbose_name="Сообщение")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='discuss_comments', verbose_name="Автор")
    discuss = models.ForeignKey(Discuss, on_delete=models.PROTECT, verbose_name="Обсуждение")

    reply = models.ForeignKey(
        'Comment', blank=True, null=True, on_delete=models.SET_NULL, related_name='answer',
        verbose_name="Ответ на сообщение"
    )

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время правки")

    likes_count = models.IntegerField(default=0, verbose_name='Да')
    dislikes_count = models.IntegerField(default=0, verbose_name='Нет')

    usefulness = models.FloatField(default=0, verbose_name='Полезность')

    def inc(self, is_liked):
        if is_liked:
            self.likes_count += 1
        else:
            self.dislikes_count += 1
        self.save()

    def dec(self, is_liked):
        if is_liked:
            self.likes_count -= 1
        else:
            self.dislikes_count -= 1
        self.save()

    def alt(self, is_liked):
        if is_liked:
            self.likes_count += 1
            self.dislikes_count -= 1
        else:
            self.likes_count -= 1
            self.dislikes_count += 1
        self.save()

    def save(self, *args, **kwargs):
        self.usefulness = get_usefulness(self.likes_count, self.dislikes_count)
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.author.username} -> {self.discuss.slug}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']


class Filter(models.Model):
    sort_by = models.SmallIntegerField(null=True, blank=True, choices=SORT_BY['discuss'], verbose_name="Сортировать по")
    sort_as = models.BooleanField(null=True, blank=True, verbose_name="Сортировать как")

    author = models.ForeignKey(
        Person, blank=True, on_delete=models.PROTECT, related_name='discuss_filter', verbose_name="Автор"
    )

    topic = models.ForeignKey(Topic, blank=True, on_delete=models.PROTECT, verbose_name="Тема")
    query = models.CharField(max_length=MAX_QUERY_LEN, blank=True, verbose_name="Поисковый запрос")

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'


class Reaction(models.Model):
    comment = models.ForeignKey(Comment, on_delete=models.PROTECT, verbose_name="Комментарий")
    person = models.ForeignKey(Person, blank=True, on_delete=models.PROTECT, verbose_name="Пользователь")

    is_liked = models.BooleanField(default=False, verbose_name='Понравился')

    def __str__(self):
        return f'{self.person.username} -> {self.comment}'

    def save(self, *args, **kwargs):
        if not self.pk:
            self.comment.inc(self.is_liked)
        else:
            self.comment.alt(self.is_liked)
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        self.comment.dec(self.is_liked)
        super().delete(*args, **kwargs)

    class Meta:
        verbose_name = 'Реакция'
        verbose_name_plural = 'Реакции'
        ordering = ['id']
