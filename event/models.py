from django.db import models

from const import MAX_LINK_LEN, MAX_TITLE_LEN
from person.models import Person


class Event(models.Model):
    link = models.CharField(blank=True, max_length=MAX_LINK_LEN, verbose_name="Ссылка")

    title = models.CharField(blank=True, max_length=MAX_TITLE_LEN, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Текст")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='events', verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.author} -> {self.title}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
        ordering = ['-create_time']
