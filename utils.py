import re
from random import randint, random, shuffle

from django.utils import timezone
from faker import Faker
from matplotlib import colors


def get_search(text):
    search = text.lower().replace('ё', 'е')
    search = re.sub(r'\W', ' ', search).strip()
    return re.sub(r' +', ' ', search)


def get_now():
    return timezone.now()


roles = {
    'admin': 'Админ',
    'user': 'Пользователь',
    'patron': 'Патрон',
    'moderator': 'Модератор'
}
categories = {
    'logic': 'Логические',
    'geometric': 'Геометрические',
    'mathematical': 'Математические',
    'children': 'Детские',
    'riddles': 'Загадки'
}

colors = list(colors.cnames.keys())
shuffle(colors)


class BaseData:
    app = ''
    ru = Faker(locale="ru_RU")
    en = Faker()

    def get_rand(self, array, field=None):
        if field is None:
            i = randint(0, len(array) - 1)
            return array[i]
        for _ in range(2):
            i = randint(0, len(array) - 1)
            if not hasattr(array[i], field):
                return array[i]

    def flip_coin(self):
        return random() > 0.5

    def get_text(self):
        return self.ru.text()

    def get_title(self):
        return self.ru.text(max_nb_chars=50)

    def get_slug(self):
        t = self.en.text(max_nb_chars=50).lower()
        t = re.sub('[^a-z]', ' ', t).strip()
        return re.sub(' +', '_', t)

    @staticmethod
    def get_roles():
        return roles.items()

    @staticmethod
    def get_categories():
        return categories.items()

    @staticmethod
    def get_username():
        return colors.pop()
