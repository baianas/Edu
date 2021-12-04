#словари

# служит для описания объектов

# словарь - неупорядоченная изменяемая последовательность элементов вида ключ: значение

# ключи в словаре должны быть неизменяемыми и уникальными

# a = {}
# b = set()
# c = dict()

# a = {'a':1, 'b':2}

# b = {[1, 2, 3]: 'value'} #ошибка

# dict1 = {'a':1, 'b': 2}
# dict2 = {1:'value', 2:'value'}
# dict3 = {(1,2,3): 1, (2,3,4): '2'}
# dict4 = {'1': 'value', 2:'value'}

# some_dict = {'a': 1, 'b': 2, 'a':3}
# print(some_dict) #{'a': 3, 'b': 2}

# headphones = {'brand': 'Hoco', 'model': 'Air v28', 'color': 'white', 'type': 'wireless'}

# # headphones['brand'] #'Hoco'
# # headphones['type'] #'wireless'
# # headphones['volume'] #KeyError

# brand = headphones.get('brand') #'Hoco'
# # print(brand)

# power = headphones.get('power', ' ')
# print(power)

#добавление элементов

# a = {'name': 'Ivan', 'last_name': 'Petrov'}

# a['age'] = 25

# # update(dict) - добавляет элементы dict в текущий словарь

# a = {'a':1, 'b':2}

# a.update({'c':3, 'd':4}) 

# a #{'a':1, 'b':2, 'c':3, 'd':4}

# b = {'a':1, 'b':2}
# b.update({'b':3, 'c':4})
# b #{'a':1, 'b':3, 'c':4}

# setdefault(key, [value]) - если ключа key нет, \
# то добавляет его в словарь со значением value, если value не указан,\
# то устанавливается значение None. Если ключ есть,\
# в словаре, то возвращает значение

# dict1 = {'key':'1', 'key2': '2'}
# # dict1.setdefault('key3')
# dict1.setdefault('key3', '3')
# print(dict1)

#изменение элементов
# a = {'name': 'Ivan', 'last_name': 'Petrov', 'age': 25}

# a['age'] = 26
# print((a))



#удаление элементов

# pop(key, [value]) - удаляет элемент по ключу и возвращает значение.\
# Если такого ключа нет и value не задан, то происходит KeyError.\
# Если value задан, то возвращается

# a = {'a':1, 'b':2, 'c':3}
# deleted = a.pop('b')
# print((deleted)) #2
# print(a) #{'a':1, 'c':3}

# a = {'a':1, 'b':2, 'c':3}
# deleted = a.pop('e') #KeyError
# print(deleted)
# print(a)

# key = 'e'
# a = {'a':1, 'b':2, 'c':3}
# deleted = a.pop(key, None)
# print(deleted)
# print(a) #{'a':1, 'b':2, 'c':3}

# popitem() - удаляет рандомный (последний) элемент

# a = {'a':1, 'b':2, 'c':3}

# deleted = a.popitem()
# print(deleted)
# print(a)

# del() - удаляет элементы по ключу

# a = {'a':1, 'b':2, 'c':3}
# del a['a']
# print(a)

# del a['d'] #KeyError

# clear() - очищает словарь
# a = {'a':1, 'b':2, 'c':3}
# a.clear()
# a #{}

# #создание (объявление) словаря

# dict1 = {}
# dict2 = dict()

# dict3 = {'a':1, 'b':2}
# dict4 = dict(a=1, b=2)
# dict5 = dict.fromkeys(['a', 'b,'], 0) #{'a':0, 'b':0}
# dict6 = dcit([('a', 1), ('b', 2)])

#keys() - возвращает ключи
# a = {'name': Jack, 'last_name': 'Jones'}

# a.keys() #dict_keys(['name', 'last_name'])

#values() - возвращает значения

# a = {'name': Jack, 'last_name': 'Jones'}

# a.values() #dict_values(['Jack', 'Jones])

# #items() - возвращает ключи и значения

# a = {'name': Jack, 'last_name': 'Jones'}

# a.items()() #dict_items([('name', 'last_name), ('Jack', 'Jones')])

#copy() - создает копию словаря

# notebooks = {
#     'brand': 'Apple',
#     'model': 'Macbook Pro',
#     'ram': 8,
#     'accesories': ['case',
#     'headphones', 'charger'],
#     'has_3.5_mm': False,
#     'dvd_drive': None,
#     'cpu': {
#         'model': 'Intel ...',
#         'frequency': '....',
#     }
# }

# a = {'a':1, 'b':2}

# #при обходе словаря, обходятся только его ключи
# for item in a:
#     print(item)

# for item in a.keys():
#     print(item)

# #обход по значениям
# for iitem in a.values():
#     print(item)

# for key in a:
#     print(a[key])

# #обход по элементам
# for item in a.items():
#     print(item[0]) #ключ
#     print(item[1]) #значение

# for key, value in a.items():
#     print(key)
#     print(value)

# a = {'Tim': 20000, 'Jack': 30000}

# for person, salary in a.items():
#     print(person)