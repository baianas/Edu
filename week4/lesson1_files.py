#файлы

#чтение
#запись

# Файлы бывают текстовые и бинарные t, b

#режим открытия файлов
# 'r' - только для чтения
# 'w' - перезапись, если файл уже существует, то содержимое стирается
# 'x' - запись в новый файл, если файл есть, выдаёт исключение FileExistsError
# 'a' - дозапись

# '+' - если файл открыт для чтения, то разрешает запись и наоборот

# open('имя либо путь к файлу', 'режим') - функция для открытия 

# file = open('/home/baianas/python_15/week4/test1.txt', 'rt')
# file = open('test1.txt')
# print(file.read())

# for line in file:
# file.read() - считывает всё содержимое в виде одной большой строки
# file.readline() - считывает по одной строке
# file.readlines() - считывает все строки в виде списка

# print(file.read())
# print(file.readline())
# print(file.readlines())

# print(file.read())
# print(file.read())

# file.readable()- проверяет, открыт ли файл для чтения

# write(str) - записывает одну строку в файл

# writelines(list) - записывает сразу несколько строк

# file2 = open('test2.txt', 'w')
# file2.write('line1\n')
# file2.write('line2\n')
# file2.writelines(['line1\n', 'line2\n'])

# file3 = open('test2.txt', 'a')
# file3.write('line3\n')
# file3.close()

#открытие файла чтения и записи

# file = open('test3', 'w+')
# file.write('test string')
# file.seek(0)
# content = file.read()
# print(content)

# seek() - перенос курсора на указанную позицию

# with open('test2.txt', 'r') as f:
#     content = f.read()
#     print(content)

# HTML, XML, YAML, JSON - фррматы обмена данными

# JSON (JavaScript Object) - формат обмена и хранения данных


# car = {
#     'brand': 'Toyota',
#     'model': 'Avalon',
#     'color': 'black',
#     'volume': 3.5, 'accessories': ('DVD', 'CruiseControl', 'Smart Card'),
#     'parking_assistant': None,
#     'has_insurance': True
# }

# Python                  JSON
# str                     string
# int, float              number
# list                    array
# tuple                   array
# dict                    object
# None                    null
# True/False              true/false

# В JSON в качестве ключей используются только строки, записываются только с двойными кавычками

# import json

# car = {
#     'brand': 'Toyota',
#     'model': 'Avalon',
#     'color': 'black',
#     'volume': 3.5,
#     'accessories': ('DVD', 'CruiseControl', 'Smart Card'),
#     'parking_assistant': None,
#     'has_insurance': True
# }

# json.dumps(python_obj) - принимает python объект (dict, list) и приводит его к формату json
# json.loads(json_obj) - принимает json объект преобразует его в python объект

# res = json.dumps(car)
# print(res)

# json_car = '{"brand": "Toyota", "model": "Avalon", "color": "black", "volume": 3.5, "accessories": ["DVD", "CruiseControl", "Smart Card"], "parking_assistant": null, "has_insurance": true}'
# res1 = json.loads(json_car)
# print(res1)


# a = {1: 'a', 2: 'b', 3: 'c'}

# print(json.dumps(a))
# #{"1": "a", "2": "b", "3": "c"}

# car = {
#     'brand': 'Toyota',
#     'model': 'Avalon',
#     'color': 'black',
#     'volume': 3.5,
#     'accessories': ('DVD', 'CruiseControl', 'Smart Card'),
#     'parking_assistant': None,
#     'has_insurance': True
# }
# import json
# file1 = open('test.json', 'w')
# res = json.dumps(car)
# file1.write(res)

# import json
# file1 = open('test.json', 'w')
# json.dump(car, file1)

# dumps(puthon_object) - вызвращает строку в json формате
# dump(python_object, file) - преобразует данные в json и записывает в файл
# loads(json_object) - возвращает в python формате
# load(file) - считывает из файла данные в формате json и преобразует их в python формате

# products = [{'title': 'Milk', 'price': 45},
#             {'title': 'Oil', 'price': 160},
#             {'title': 'Cup', 'price': 60, 'color': 'red'}]

# import json
# res = json.dumps(products)
# print(res)

# CSV(Comma-Separated Values)

# with open('test1.txt', 'r') as file1, open('test2.txt', 'w') as file2:
#     file1.read()
#     file2.write()

# name1 = 'string2'

# модуль - файл с расширением .py
# пакет - директория, которая может вклычаьб в себя другие директории, 
# но она также должна содержать файл __init__.py

# from test_folder.test1 import func1