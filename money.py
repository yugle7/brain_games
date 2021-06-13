import json

import requests

api_access_token = ''  # токен можно получить здесь https://qiwi.com/api
my_login = ''  # номер QIWI Кошелька в формате +79991112233

s = requests.Session()
s.headers['authorization'] = 'Bearer ' + api_access_token
parameters = {'rows': '10'}
h = s.get('https://edge.qiwi.com/payment-history/v1/persons/' + my_login + '/payments', params=parameters)
print(json.loads(h.text))

# https://developer.qiwi.com/ru/qiwi-wallet-personal/index.html#autocomplete
