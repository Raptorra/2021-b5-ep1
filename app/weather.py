from datetime import datetime
import os
import pytz
import requests
import math


secrets = secretmanager.SecretManagerServiceClient()

PROJECT_ID = 'enigma4-290909'

API_KEY = secrets.access_secret_version("projects/"+PROJECT_ID+"/secrets/weather-api-key/versions/latest").payload.data.decode("utf-8")
API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data