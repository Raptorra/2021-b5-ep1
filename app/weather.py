from datetime import datetime
import os
import pytz
import requests
import math
from google.cloud import secretmanager

API_KEY = ""

if API_KEY is None or API_KEY == "":
    PROJECT_ID = 'enigma4-290909'
    secrets = secretmanager.SecretManagerServiceClient()
    API_KEY = secrets.access_secret_version("projects/"+PROJECT_ID+"/secrets/weather-api-key/versions/1").payload.data.decode("utf-8")

API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data