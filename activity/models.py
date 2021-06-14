from django.db import models

from person.models import Person


class Activity(models.Model):
    KIND = (
        (1, 'discuss'),
        (2, 'puzzle'),
    )
    kind = models.SmallIntegerField(null=True, blank=True, choices=KIND, verbose_name="Тип")

    title = models.CharField(blank=True, verbose_name="Заголовок")
    text = models.TextField(blank=True, verbose_name="Текст")
    link = models.CharField(blank=True, verbose_name="Ссылка")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='activities', verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")

    def __str__(self):
        return f'{self.author} -> {self.text}'

    class Meta:
        verbose_name = 'Активность'
        verbose_name_plural = 'Активности'
        ordering = ['id']
