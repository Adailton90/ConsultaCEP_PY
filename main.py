import requests
import json


def consultaCEP(cep):
    response = requests.get(f'https://viacep.com.br/ws/{cep}/xml/')
    return response.text