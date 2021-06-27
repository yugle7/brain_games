from django.db import models
from django.urls import reverse

from comment.models import Comment, Talk
from const import *
from person.models import Person
from utils import *


class Category(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)
    name = models.CharField(max_length=MAX_TITLE_LEN, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{reverse("puzzle-list")}?category={self.slug}'

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']


class Puzzle(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)
    title = models.CharField(max_length=MAX_TITLE_LEN, verbose_name="Название")

    text = models.TextField(blank=True, verbose_name="Условие")
    notes = models.TextField(blank=True, verbose_name="Примечания")
    reference = models.TextField(blank=True, verbose_name="Эталонное решение")
    search = models.TextField(blank=True, verbose_name="Поиск")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    public_talk = models.OneToOneField(
        Talk, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='public_puzzle', verbose_name='Уточнение условий'
    )
    private_talk = models.OneToOneField(
        Talk, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='private_puzzle', verbose_name='Обсуждение решения'
    )

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время правки")

    is_published = models.BooleanField(null=True, blank=True, verbose_name="Опубликована")

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    weight = models.SmallIntegerField(default=0, verbose_name="Вес")

    interest = models.FloatField(default=0, verbose_name='Интерес')
    complexity = models.FloatField(default=0, verbose_name='Сложность')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('puzzle-detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.search = get_search(self.title + ' ' + self.text)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id']
