from django.db import models

from person.models import Person


class Talk(models.Model):
    class Meta:
        verbose_name = 'Разговор'
        verbose_name_plural = 'Разговоры'
        ordering = ['id']


class Comment(models.Model):
    text = models.TextField(blank=True, verbose_name="Текст")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Автор")
    talk = models.ForeignKey(Talk, on_delete=models.PROTECT, verbose_name="Разговор")

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    edit_time = models.DateTimeField(auto_now=True, verbose_name="Время правки")

    def __str__(self):
        return f'{self.author} -> {self.text}'

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
