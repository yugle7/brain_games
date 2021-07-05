from django.db import models

from const import MAX_LINK_LEN, MAX_SLUG_LEN, MAX_TITLE_LEN
from person.models import Person


class Tag(models.Model):
    slug = models.SlugField(max_length=MAX_SLUG_LEN, unique=True, db_index=True)
    name = models.CharField(max_length=MAX_TITLE_LEN, db_index=True, verbose_name="Название")

    def __str__(self):
        return f'#{self.slug}'

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'


class Activity(models.Model):
    tags = models.ManyToManyField(Tag, null=True, blank=True, verbose_name="Теги")
    link = models.CharField(blank=True, max_length=MAX_LINK_LEN, verbose_name="Ссылка")

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
