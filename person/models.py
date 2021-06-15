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
        return f'{reverse("person-list")}?role={self.slug}'

    class Meta:
        verbose_name = 'Роль'
        verbose_name_plural = 'Роли'
        ordering = ['id']


class Person(AbstractUser):
    friends = models.ManyToManyField('Person', blank=True, verbose_name="Друзья")

    role = models.ForeignKey(Role, null=True, blank=True, on_delete=models.PROTECT, verbose_name="Роль")
    about = models.TextField(verbose_name="О себе")
    search = models.TextField(blank=True, verbose_name="Поиск")

    last_visit_time = models.DateTimeField(blank=True, null=True, verbose_name="Время последнего посещения")

    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    contribution = models.IntegerField(default=0, verbose_name='Вклад')
    money = models.IntegerField(default=0, verbose_name='Счет')

    def __str__(self):
        return self.username

    def get_absolute_url(self):
        return reverse('person-detail', kwargs={'pk': self.pk})

    def save(self, *args, **kwargs):
        self.search = get_search(self.about.lower())
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ['id']
