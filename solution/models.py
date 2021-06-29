from django.db import models
from django.urls import reverse

from comment.models import Comment, Talk
from person.models import Person
from puzzle.models import Puzzle, Category
from utils import *


class Solution(models.Model):
    puzzle = models.ForeignKey(Puzzle, on_delete=models.PROTECT, verbose_name="Задача")

    solver = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Решающий")
    checker = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='checks', verbose_name="Проверяющий")

    text = models.TextField(blank=True, verbose_name="Ответ")
    talk = models.OneToOneField(Talk, blank=True, null=True, on_delete=models.SET_NULL)

    is_accepted = models.BooleanField(default=False, verbose_name="Решение зачтено")
    is_submitted = models.BooleanField(default=False, verbose_name="Ответ отправлен")

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

