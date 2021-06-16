from django.db import models
from django.urls import reverse

from comment.models import Comment
from person.models import Person
from puzzle.models import Puzzle, Category
from utils import *


class Solution(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.PROTECT, verbose_name="Задача")
    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")

    answer = models.ForeignKey('Answer', on_delete=models.PROTECT, verbose_name="Ответ")

    is_accepted = models.BooleanField(blank=True, null=True, verbose_name="Зачтена")
    is_submitted = models.BooleanField(default=False, verbose_name="Отправлено на проверку")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    reward = models.IntegerField(default=0, verbose_name='Награда за проверку')

    def __str__(self):
        return f'{self.author} -> {self.puzzle}'

    def get_absolute_url(self):
        return reverse('solution-detail', kwargs={'id': self.id})

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class Answer(models.Model):
    solution = models.ForeignKey(Solution, on_delete=models.PROTECT, verbose_name="Решение")
    text = models.TextField(blank=True, verbose_name="Ответ")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    is_accepted = models.BooleanField(default=False, null=True, verbose_name="Зачтен")

    def __str__(self):
        return f'{self.solution} -> {self.text}'

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Review(models.Model):
    answer = models.ForeignKey(Answer, on_delete=models.PROTECT, verbose_name="Ответ")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Проверяющий")
    text = models.TextField(blank=True, verbose_name="Отзыв проверяющего")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    update_time = models.DateTimeField(auto_now=True, verbose_name="Время обновления")

    is_accepted = models.BooleanField(blank=True, null=True, verbose_name="Зачтен")

    def __str__(self):
        return f'{self.author} -> {self.answer}'

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class Talk(models.Model):
    comment = models.ForeignKey(
        Comment, on_delete=models.PROTECT, related_name='solution_talk', verbose_name="Комментарий"
    )
    solution = models.ForeignKey(Solution, on_delete=models.PROTECT, verbose_name="Решение")

    def __str__(self):
        return f'{self.comment} -> {self.solution}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
