from datetime import datetime
import os
import pytz
import requests
import math


with open('api_key.txt', 'r') as file:
    API_KEY = file.read().replace('\n', '')
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data