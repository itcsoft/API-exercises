import json
import requests

city_name = "Ташкент"
API_key = '6621546e1a94625a215c063e4320d66d'
API_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&appid={API_key}'

response = requests.get(API_url)
print(response)
json_data = response.json()
# print(type(json_data))
status_sky = json_data['weather'][0]['main']
print(status_sky)
temp = json_data['clouds']
# print(temp)
dic = {"clear":"чистое", "snow":"снежное", "rain":"дождь", "wind":"ветер", "clouds":"облака", "foggy":"туман"}

if status_sky.lower() in dic:
  print("Cостояние:",dic[status_sky.lower()])
else:
  print("Cостояние:", status_sky)





d = {
    'main':{
      'color':'blue',
      'cat':3,
      'say':[
        'Hi', 'I', 'like'
    ]
}}

# print(d['main']['color'])
# print(d['main']['say'][1])