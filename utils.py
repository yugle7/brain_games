import csv
import re
from random import randint, random

from django.utils import timezone


def get_search(text):
    search = text.lower().replace('ё', 'е')
    search = re.sub(r'\W', ' ', search).strip()
    return re.sub(r' +', ' ', search)


def get_now():
    return timezone.now()


class BaseData:
    app = ''

    def get_rand(self, array):
        i = randint(0, len(array) - 1)
        return array[i]

    def flip_coin(self):
        return random() > 0.5

    def get_data(self, name):
        return csv.reader(open(f'{self.app}/objects/{name}.csv'))
