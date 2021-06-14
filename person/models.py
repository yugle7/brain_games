from django.contrib.auth.models import User, AbstractUser
from django.db import models
from django.urls import reverse, reverse_lazy

from const import *
from utils import *


class Role(models.Model):
    name = models.CharField(max_length=MAX_TITLE_LEN, db_index=True, verbose_name="Название")
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'{reverse("person_list")}?role={self.slug}'

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['id']


class Person(AbstractUser):
    friends = models.ManyToManyField('Person', blank=True, verbose_name="Друзья")
    bans = models.ManyToManyField('Person', blank=True, related_name='banned_by', verbose_name="Забаненные")

    role = models.ForeignKey(
        Role, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Роль"
    )
    about = models.TextField(verbose_name="О себе")

    last_visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время последнего посещения")
    search = models.TextField(blank=True, verbose_name="Поиск")

    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    contribution = models.IntegerField(default=0, verbose_name='Вклад')
    money = models.IntegerField(default=0, verbose_name='Счет')

    solutions_opened = models.IntegerField(default=0, verbose_name='Решает задач')
    solutions_closed = models.IntegerField(default=0, verbose_name='Решено задач')
    puzzles_offered = models.IntegerField(default=0, verbose_name='Предложил задач')
    reviews_opened = models.IntegerField(default=0, verbose_name='Задач проверяет')
    reviews_closed = models.IntegerField(default=0, verbose_name='Задач проверил')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('show_person', kwargs={'pk': self.pk})

    # solutions_url

    def get_solutions_url(self, is_accepted):
        return f'{reverse_lazy("solution_list")}?author={self.pk}&is_accepted={int(is_accepted)}'

    def get_closed_solutions_url(self):
        return self.get_solutions_url(True)

    def get_opened_solutions_url(self):
        return self.get_solutions_url(False)

    # reviews_url

    def get_reviews_url(self, is_accepted):
        return f'{reverse_lazy("solution_list")}?reviewer={self.pk}&is_accepted={int(is_accepted)}'

    def get_closed_reviews_url(self):
        return self.get_reviews_url(True)

    def get_opened_reviews_url(self):
        return self.get_reviews_url(False)

    def get_puzzles_url(self):
        return f'{reverse_lazy("puzzle_list")}?author={self.pk}'

    def save(self, *args, **kwargs):
        self.search = get_search(self.about.lower())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']


class Filter(models.Model):
    sort_by = models.SmallIntegerField(null=True, blank=True, choices=SORT_BY['person'], verbose_name="Сортировать по")
    sort_as = models.BooleanField(default=True, verbose_name="Сортировать как")

    person = models.ForeignKey(Person, null=True, blank=True, on_delete=models.SET_NULL, verbose_name="Пользователь")

    is_friend = models.BooleanField(default=False, verbose_name="Друг")
    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Роль")

    query = models.CharField(max_length=MAX_QUERY_LEN, blank=True, verbose_name="Поисковый запрос")

    class Meta:
        verbose_name = 'Фильтр'
        verbose_name_plural = 'Фильтры'
        ordering = ['id']


class Talk(models.Model):
    is_public = models.BooleanField(default=True, verbose_name="Публичные")

    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Человек")
    comment = models.ForeignKey('Comment', on_delete=models.PROTECT, verbose_name="Комментарий")

    def __str__(self):
        return f'{self.comment.author} -> {self.person}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
