import requests
from googletrans import Translator

city_name = "Ош"
API_key = '6621546e1a94625a215c063e4320d66d'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'

res = requests.get(API_url)
json_data = res.json()
status_sky = json_data['weather'][0]['main']
translator = Translator()
a = translator.translate(status_sky, dest='ja').text
b = translator.translate(city_name, dest='ja').text
# print(status_sky)

print(a, "°C")
print(a, b)