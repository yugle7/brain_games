from django.db import models
from django.urls import reverse

from person.models import Person


class Comment(models.Model):
    text = models.TextField(verbose_name="Сообщение")

    author = models.ForeignKey(Person, on_delete=models.PROTECT, related_name='person_comments', verbose_name="Автор")
    person = models.ForeignKey(Person, on_delete=models.PROTECT, verbose_name="Пользователь")

    reply = models.ForeignKey(
        'Comment', blank=True, null=True, on_delete=models.SET_NULL, related_name='answer',
        verbose_name="Ответ на сообщение"
    )

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")

    is_liked = models.BooleanField(default=False, verbose_name='Понравился автору')
    is_hidden = models.BooleanField(default=False, verbose_name='Автор скрыл')

    def __str__(self):
        return f'{self.author} -> {self.person}'

    def get_like_url(self):
        return reverse('comment_like', kwargs={'pk': self.pk})

    def get_hide_url(self):
        return reverse('comment_hide', kwargs={'pk': self.pk})

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['id']
