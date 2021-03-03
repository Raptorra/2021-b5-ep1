import requests

try:
    import app.api_key
    API_KEY = app.api_key.value
except BaseException as e:
    from google.cloud import secretmanager_v1
    PROJECT_ID = '675857481503'
    secret_name = 'weather-api-key'
    secrets = secretmanager_v1.SecretManagerServiceClient()
    secret_version_name = f'projects/{PROJECT_ID}/secrets/{secret_name}/versions/latest'
    API_KEY = secrets.access_secret_version(name=secret_version_name).payload.data.decode("utf-8")

API_URL = ('http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&appid={}')


def query_api(city):
    try:
        print(API_URL.format(city, API_KEY))
        data = requests.get(API_URL.format(city, API_KEY)).json()
    except Exception as exc:
        print(exc)
        data = None
    return data
