from django.db import models
from django.urls import reverse

from const import *
from person.models import Person
from utils import *


class Category(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)
    name = models.CharField(max_length=MAX_TITLE_LEN, db_index=True, verbose_name="Категория")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{reverse("puzzle_list")}?category={self.slug}'

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

    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время правки")

    is_published = models.BooleanField(null=True, blank=True, verbose_name="Опубликована")

    category = models.ForeignKey(Category, on_delete=models.PROTECT, verbose_name="Категория")
    weight = models.SmallIntegerField(default=0, verbose_name="Вес")

    looked_count = models.IntegerField(default=0, verbose_name='Видело')
    answered_count = models.IntegerField(default=0, verbose_name='Ответило')
    solved_count = models.IntegerField(default=0, verbose_name='Решило')

    one_try = models.IntegerField(default=0, verbose_name='С первой попытки')
    two_tries = models.IntegerField(default=0, verbose_name='За две попытки')
    three_tries = models.IntegerField(default=0, verbose_name='За три попытки')
    many_tries = models.IntegerField(default=0, verbose_name='Много попыток')

    likes_count = models.IntegerField(default=0, verbose_name='Понраилась')
    dislikes_count = models.IntegerField(default=0, verbose_name='Не понравилась')
    stars_count = models.IntegerField(default=0, verbose_name='В избранном')

    interest = models.FloatField(default=0, verbose_name='Интерес')
    complexity = models.FloatField(default=0, verbose_name='Сложность')

    def set_complexity(self):
        if self.answered_count > 10 and self.looked_count > 100:
            solves_count = self.one_try + self.two_tries / 2 + self.three_tries / 4 + self.many_tries / 8
            answers_count = self.answered_count + self.looked_count / 5
            self.complexity = 1 - solves_count / answers_count

    def set_interest(self):
        if self.solved_count > 2:
            self.interest = (self.stars_count + self.likes_count - 2 * self.dislikes_count) / self.solved_count

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('show_puzzle', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.search = get_search(self.title + ' ' + self.text)
        self.set_complexity()
        self.set_interest()
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['id']


class Filter(models.Model):
    sort_by = models.SmallIntegerField(default=1, choices=SORT_BY['puzzle'], verbose_name="Сортировать по")
    sort_as = models.BooleanField(default=True, verbose_name="Сортировать как")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='puzzle_filter', verbose_name="Автор")

    is_solved = models.BooleanField(null=True, blank=True, verbose_name="Решена")
    is_published = models.BooleanField(default=True, verbose_name="Опубликована")

    category = models.ForeignKey(Category, null=True, on_delete=models.PROTECT, verbose_name="Категория")
    query = models.CharField(max_length=MAX_QUERY_LEN, verbose_name="Поисковый запрос")

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'
        ordering = ['id']


class Comment(models.Model):
    kind = models.SmallIntegerField(null=True, choices=COMMENT_KIND)
    text = models.TextField(blank=True, verbose_name="Сообщение")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='puzzle_comments', verbose_name="Автор")
    puzzle = models.ForeignKey(Puzzle, on_delete=models.PROTECT, verbose_name="Задача")

    reply = models.ForeignKey(
        'Comment', blank=True, null=True, on_delete=models.PROTECT, related_name='answer',
        verbose_name="Ответ на сообщение"
    )

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="Время правки")

    def __str__(self):
        return f'{self.author} -> {self.puzzle}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
