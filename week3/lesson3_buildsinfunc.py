#встроенные функции

# int()
# float()
# list()
# str()
# tuple()
# bool()
# dict()
# set()
# frozenset()

# a = [1, 2, 3, 4]
# str(a) #'[1, 2, 3, 4]'

# b = {1, 2, 3, 4}
# str(b) #{1, 2, 3, 4}

# abs(number) возвращает абсолютное значение(модуль) числа

# a1 = 20
# a2 = -10

# abs(a1) #20
# abs(a2) #10

# all(iterable), any(iterable)

# all(iterable) - проверяет, что все элементы являются истинными -> and

# any(iterable) - проверяет, что хотя бы один элемент является истинным -> or

# a1 = [1, 2, 3, 4]
# a2 = [1, 10, 0, 19]

# all(a1) #True
# a1[0] and a1[1] and a1[2] and a1[3] #True

# any(a2) #True
# a1[0] or a1[1] or a1[2] or a1[3] #True

# all(a2) #False

#перевод числа в разные системы счисления
# bin(number: int) #двочиная система
# oct(number: int) #восьмеричная система
# hex(number: int) #шестнадцатеричная система
# int()- десятеричная система

# a = 20
# bin(a) #'0b10100'
# oct(a) #'0o24'
# hex(a) #'0x14

# hex_a = '0x14'
# print(int(hex_a, 16))

# chr(), ord()

# ord(symbol) - возвращает номер символа в таблице ascii

# symbol = 'a'
# ord(symbol) #97

# chr(num) - по номеру возвращает символ
# num = 97
# chr(num) #'a'

# dir(obj) - выдает список методов

# a = 'string'
# print(dir(a)) 

# eval() - выполнение выражений
# a = 'print(10)'
# a2 = 'raise ValuError'

# eval(a2)

# exec() - проверяет и выполняет блок кода

# a = 'a1 = (1, 2, 3, 4)\nfor num in a1:\n\tprint(num * 10)'
# exec(a)

# help(obj) - справка по объекту
# id(obj) - выдаёт адрес объекта в памяти
# isinstance(obj, class_) - проверяет, является объект экземпляром определенного класса
# a = 'str'
# isinstance(a, str) #True

# type(obj) - выдает название класса, к которому относится
# type(a) #'class: str'
# type(a) == str #True

# max(), min(), sum()

# max(iterable) - максимальный элемент
# min(iterable) - минимальный объект
# sum(iterable) - сумма элементов

# object() - возвращает пустой объект

# open() - открывает файлы для чтения/записи

# pow(x, y) - возвожит х в степень у, х ** у
# pow(x, y, z) -> (x ** y) % z

#round(float) - округляет число
# a = 5.24756
# round(a) #5
# round(a, 3) #5.248

# slice(x, y, z) - создаёт срез
# a = [1, 2, 3, 4, 5]
# a[1:4] #[2, 3, 4]
# s = slice(1, 4)
# print(a[s]) #[2, 3, 4]

# sorted(list) #сортирует элементы списка(по умолч. по возрастанию)

# a1 = [2, 1, 3, 4]
# a2 = ['Tim', 'John', 'Jack', 'Maria']

# sorted(a1) #[1, 2, 3, 4]
# sorted(a2) #['Jack', 'John', 'Maria', 'Tim']

# sorted(a1, reverse=True) #[4, 3, 2, 1]
# print(sorted(a2, key=len)) #['Tim', 'John', 'Jack', 'Maria']

# reversed(list) - расставляет элементы в обратном порядке
# a = [4, 2 ,10]
# reversed(a) #[10, 2, 4]
# a[::-1] #[10, 2, 4]

# enumerate(), map(), filter(), reduce(), zip()

# enumerate(iterable, [start]) - пронумеровывает элементы последовательности

# a = ['Alla', 'Nik', 'Kate']
# enumerate(a) #[(0, 'Alla'), (1, 'Nik'), (2, 'Kate')]

# enumerate(a, start=1) #[(1, 'Alla'), (2, 'Nik'), (3, 'Kate')]

# Функция - именованный блок кода

# def my_func(num):
#     return num * 5

# res = my_func(20)
# res #100

# lambda num: num * 5

# анонимные функции используют, чтобы объявить функцию на месте её использования

# map(func, iterable) - применяет функцию к каждому элементу, возвращает новый итерируемый объект

# from typing import Iterable


# a = [1, 2, 3, 4, 5]

# def square(num):
#     return num ** 2

# res = []
# for num in a:
#     res.append(square(num))

# print(res)

# res = [square(num) for num in a] #[1, 4, 9, 16, 25]

# res = list(map(square, a)) #map_object
# res = map(lambda num: num ** 2, a)
# print(res)

# filter(filter_func, iterable) - фильтрация элементов последовательности

# a = [29, 32, 44, 44, 11, 345, 21, 345, 23, 45, 77, 89, 871]
# # [345, 21, 345, 45]
# def filter_func(num):
#     return num % 3 == 0

# res = []
# for num in a:
#     if filter_func(num):
#         res.append(num)

# res = [num for num in a if filter_func(num)]

# res = filter(filter_func, a)
# res = filter(lambda num: num % 3 == 0, a)

# from functools import reduce
# reduce(function, iterable) - элементы последовательности сводятся к одному значению
# минимальный элемент, максимальный элемент, сумма, произведение элементов, факториал
# 
# a = ('Tim', 'Jane', 'Andy', 'Kyle')

# min_element = reduce(lambda x, y : x if x < y else y, a)

# print(min_element)

# min(a) #'Andy'

# zip(*iterables) - связывает между собой элементы разных последовательностей

# a1 = ['a', 'b', 'c']
# a2 = [1, 2, 3]

# zip(a1, a2) #[('a', 1), ('b', 2), ('c', 3)] 

#работает только до тех пор, пока не исчерпается самая короткая последовательность

# a1 = ['a', 'b', 'c', 'd']
# a2 = [1, 2, 3, 4, 5]

# zip(a1, a2) #[('a', 1), ('b', 2), ('c', 3), ('d', 4)] 

# a1 = [1, 2, 3, 4]
# print(sorted(a1))
# print(list(reversed(a1)))