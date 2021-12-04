#try - except

# Бывает 2 типа ошибки: ошибки(error) и исключения(exceptions)

# ошибки - это когда код неправильно написан синтаксически (забыли запятую, забыли скобку, забыли отступю, табуляция)

# SyntaxError - ошибка синтаксиса

# a = [1, 2, 3]
# for i in a:
#     print(i) #ошибка

# num = 10
# if num = 10:
#     print('Ok')

# IndentationError - ошибка отступа (не хватает отступа, лишний отступ)

# num = 10
#     print(num( * 10)) # IndentationError

# num = 10
# if num % 2 == 0:
#     print(('Good!'))

# TabError - смешивание табуляции и пролов

# a = [1, 2, 3]
# if len(a) > 6:
#     print('Ok')
#   else:
#       print('Not ok')

# исключения (exceptions) - возникают в случае, 
# если код написан верно, но есть проблемы с данными, 
# с памятью, с подключением и т.д

# Exception
# NameError - нет такого имени (переменной, функции, класса)

# print(my_var) #NameError

# TypeError - тип объекта не подходит для операции

# a1 = 1
# a2 = '2'

# print(a1 / a2) #TypeError

# ValueError - тип объекта правильный, но неподходящее значение

# a1 = '12'
# a2 = 'abc'

# int(a1) #12
# int(a2) #ValueError

# IndexError - обращение по несществующему индексу

# a = [1, 2, 3, 4]
# a[3] #4
# a[4] #IndexError

# KeyError - обращение по несществующему ключу

# a = {'a': 1, 'b': 2}
# a['c'] #KeyError

# a.pop('d') #KeyError

# b = {1, 2, 3}
# b.remove(10) #KeyError

# ZeroDivisionError - деление на 0

# AttributeError - обращение к несуществующему свойству или методу

# a = (1, 2, 3, 4, 5)
# a.append(6) AttributeError

# AssertionError - провал проверки assert

# assert - оператор для проверки выражений

# num = 20
# assert num > 10

# ModuleNotFoundError  - когда не найден модуль для импорта
# ImportError - модуль найден, но не найден объект для импорта (переменная, функция, класс)

# from maht import sqrt
#ModuleNotFunError

# from math import sinus
#ImportError

# a1 = 10
# a2 = 0

# print(a1 / a2)

# print('Конец программы')

#обработка исключений (try except)

# ошибки не обрабатываются при помощи try except, можно обработать только исключения

# try:
#     a = [2, 3, 4, 5]
#     for num in a:
#         print(num * 10)
# except SyntaxError:
#     print('Произошла ошибка')

# try:
#     # пробуем определенное действие
# except Exception:
#     # обрабатываем возможное исключение
# except Exception:
#     # обрабатываем возможное исключение
# else:
#     # если в блоке try  не возникло исключений
# finally:
#     # срабатывает в любом случае


# a1 = 10
# a2 = '20'

# try:
#     print(a1 + a2)
# except TypeError:
#     print('Можно сложить 2 числа или 2 строки')

# a1 = 10
# a2 = '20'
# a3 = 0

# try:
#     print(a1 / a2)
#     print(a1 / a3)
# except TypeError:
#     print('Можно делить только числа')
# except ZeroDivisionError:
#     print('Нельзя делить на 0')

# try:
#     print(a1 / a2)
#     print(a1 / a3)
# except (TypeError, ZeroDivisionError):
#     print('Произошла ошибка')

# try:
#     print(a1 / a2)
#     print(a1 / a3)
# except:
#     print('Произошла ошибка')

# try:
#     print(a1 / a2)
#     print(a1 / a3)
# except Exception as exc:
#     print(exc)
#     # print('Произошла ошибка')

# a = {'a': 1, 'b': 2}
# a['c'] #KeyError

# try:
#     value = a['c']
# except KeyError:
#     value = 0

# value = 0
# if 'c' in a:
#     value = a['c']

# value = a.get('c', 0)

# a1 = 10
# a2 = 0

# try:
#     print(a1 / a2)
# except ZeroDivisionError:
#     ...

# if a2:
#     print(a1 // a2)

# a1 = '123'
# a2 = 'abc'

# try:
#     a1 = int(a1)
#     a2 = int(a2)
# except ValueError:
#     ...


# if a1.isdigit():
#     a1 = int(a1)
# if a2.isdigit():
#     a2 = int(a2)

# a = [1, 2, 3, 4, 5]
# last_index = len(a) #= -1

# a = ['a', 'b', 'c', 'd']

# sum(a)

# a1 = '123'
# a2 = '10.5'

# print(float(a1))
# print(float((a2)))

# print(int(a1))
# print(float((a2)))




# итерируемый объект - объект, который обходится циклом for 
# (строка, словарь, множества)

# итератор - частный случай генератора. Порождает значения в цикле

# a = [1, 2, 3, 4, 5] #итерируемый объект
# b = range(1, 6) #итератор

# print(next(a))
# print(next(b))
