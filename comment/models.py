from django.db import models

from const import *
from person.models import Person


class Comment(models.Model):
    kind = models.SmallIntegerField(null=True, choices=COMMENT_KIND)
    text = models.TextField(blank=True, verbose_name="Сообщение")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='comments', verbose_name="Автор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="Время правки")

    def __str__(self):
        return f'{self.author} -> {self.puzzle}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']

