from django.db import models

from const import MAX_LINK_LEN, MAX_NAME_LEN


class Page(models.Model):
    name = models.CharField(max_length=MAX_NAME_LEN, verbose_name="Название")
    link = models.CharField(max_length=MAX_LINK_LEN, verbose_name="Ссылка")
    icon = models.CharField(max_length=MAX_LINK_LEN, verbose_name="Иконка")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Страница'
        verbose_name_plural = 'Страницы'
