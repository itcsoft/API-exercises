import re
import requests

# url = "https://oc.kg/"
# res = requests.get(url) 
# print(res)   # код статуса
# html_code = res.text
# print(res.content)      
# print(res.headers)

# print("Статуса кода:",res.status_code)
# print("Тип запроса:",res.request)
# print("Тип запроса:",res.request.method)
# print("URL сайта:",res.url)
# print("Тип кодировки(юникод)",res.encoding)
# print("Контент сайта",res.content)
# print(res.links)
# print(type(res.links))



"""open()"""
# r
# w
# a
# x

# создать файл
# my_file = open("my_file.txt", "x")

# записать в файл
# my_file2 = open("new_file.txt", "a")
# my_file2.write("Hello world!!!\n")
# my_file2.close()

# добавить запись в конце
# my_file3 = open("new_file.txt", "w")
# my_file3.write("H..........\n")
# my_file3.close()

# my_file4 = open("new_file.txt", "a+")
# my_file4.write("Python\n")
# print(my_file4.read())
# my_file4.close()





# my_file6 = open("new_file.txt", 'a+')      # для записи и чтения  
# my_file6.write("New words")
# my_file6.read()
# my_file6.close()

# my_file5 = open("new_file.txt", "r")
# print(my_file5.read())
# for i in my_file5:
#     print(i, "good")

# m = my_file5.readlines()
# print(m)
# print(type(m))

# c = 0
# y = 0
# for i in m:
#     for letter in i:
#         if letter.lower() == "h":
#             c += 1
#         elif letter.lower() == "y":
#             y += 1

# print("h:",c)
# print("y:", y)


# создать файл
# my_file = open("my_file.txt", "x")

# # Исключение
# file_name = input("Напишите название для создания файла: ")

# try:
#     new = open(file_name, "x")
#     print("Файл создан")

# except FileExistsError:
#     print("Такой файл уже существует!!!")


# o = open("new_file.txt", "w", encoding="UTF-8")
# o.write("Всем привет!   !!  \n")
# o.write("Всем привет!!!")
# o.close()

# o2 = open("new_file.txt", "r")
# print(o2.read())
# print(o2.readlines())     # list
# print(o2.readline())      # str
# print(o2.read(4))



# import os

# os.remove("s")            # remove file
# os.rmdir("nnnnnnnnnn")    # remove directory

# os.mkdir("myy")             # создать папку

# file = input("file name")
# text = input("text")

# # 4
# g = open(file, "w")
# g.write(text)

# u = input("Вставьте ссылку сайта")
# u2 = input("Введите название сайта:")+'.html'
# print(u2)

import requests

url = 'https://nurbek20.github.io/Wildlife/'
# url = input("Вставьте сслыку: ")
response = requests.get(url)
# print(response.text)

html_name = input("Введите название файла: ")+'.html'
html_file = open(html_name, 'x', encoding='UTF-8')
html_file2 = open(html_name, 'w', encoding='UTF-8')
html_file2.write(response.text)
html_file2.close()
html_file.close()
# print(type(response.text))

# lines = 0
# for i in open(html_name):
#     lines += 1
# print(lines)

images = 0
btns = 0

for i in open(html_name):
    if "<button" in i:
        btns += 1
    elif "<img" in i:
        images += 1
print("Количество изображений: ",images)
print("Количество кнопок: ",btns)
