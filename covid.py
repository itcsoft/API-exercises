from turtle import pen
import requests

country = input("Название страны: ")
url = f"https://covid-api.mmediagroup.fr/v1/cases?country={country}"
res = requests.get(url)

# print(res.text)
print("Подтверждено:",res.json()['All']['confirmed'])
print("Умерли:",res.json()['All']['deaths'])
print("Население:",res.json()['All']['population'])
# print(res.json()['All'])
city = input("Название города: ")

if city in res.json():
    print("Подтверждено:",res.json()[city]['confirmed'])
    print("Умерли:",res.json()[city]['deaths'])

else:
    print("Нет информации о городе")
