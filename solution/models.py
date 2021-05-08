from django.db import models
from django.urls import reverse

from person.models import Person
from puzzle.models import Puzzle, Category
from utils import *


class Solution(models.Model):
    draft = models.TextField(blank=True, verbose_name="Черновик")
    prev = models.TextField(blank=True, verbose_name="Старое решение")
    text = models.TextField(blank=True, verbose_name="Решение")
    review = models.TextField(blank=True, verbose_name="Отзыв проверяющего")

    puzzle = models.ForeignKey(Puzzle, on_delete=models.PROTECT, verbose_name="Задача")
    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    reviewer = models.ForeignKey(
        Person, null=True, blank=True, related_name='reviews', on_delete=models.PROTECT, verbose_name="Проверяющий"
    )

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    submit_time = models.DateTimeField(blank=True, null=True, verbose_name="Отпрвлено на проверку")
    accept_time = models.DateTimeField(blank=True, null=True, verbose_name="Зачтена")

    is_liked = models.BooleanField(null=True, blank=True, verbose_name='Понравилась')
    star = models.BooleanField(default=False, verbose_name='В избранном')

    tries_count = models.IntegerField(default=0, verbose_name='Попыток')
    reward = models.IntegerField(default=0, verbose_name='Награда')

    def to_submit(self):
        self.submit_time = timezone.now()
        self.text, self.prev = self.draft, self.text

    def to_accept(self):
        self.accept_time = timezone.now()

    def __str__(self):
        return f'{self.author.username} -> {self.puzzle.slug}'

    def get_absolute_url(self):
        return reverse('show_solution', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'
        ordering = ['-reward', 'submit_time']


class Filter(models.Model):
    person = models.ForeignKey(
        Person, blank=True, on_delete=models.PROTECT, related_name='solution_filter', verbose_name="Пользователь"
    )
    puzzle = models.ForeignKey(
        Puzzle, blank=True, on_delete=models.PROTECT, related_name='solution_filter', verbose_name="Задача"
    )
    on_review = models.BooleanField(default=False, verbose_name="Взята на проверку")
    is_submitted = models.BooleanField(default=True, verbose_name="Отправлена на проверку")
    is_accepted = models.BooleanField(default=False, verbose_name="Зачтена")

    category = models.ForeignKey(
        Category, null=True, on_delete=models.PROTECT, related_name='solution_filter', verbose_name="Категория задач"
    )

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'
