from django.db import models

from const import MAX_URL_LEN, MAX_TITLE_LEN
from person.models import Person

KIND = (
    (1, 'discuss'),
    (2, 'puzzle'),
)


class Activity(models.Model):
    kind = models.SmallIntegerField(null=True, blank=True, choices=KIND, verbose_name="Тип")
    link = models.CharField(blank=True, max_length=MAX_URL_LEN, verbose_name="Ссылка")

    title = models.CharField(blank=True, max_length=MAX_TITLE_LEN, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Текст")
    search = models.TextField(blank=True, verbose_name="Поиск")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='activities', verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.author} -> {self.title}'

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'
        ordering = ['-create_time']
