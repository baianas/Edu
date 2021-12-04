# Task1
# class Soda:
#     def __init__(self, gas):
#         self.gas = gas

#     def show_my_drink(self):
#         if self.gas:
#             print(f'Газировка и {self.gas}')
#         else:
#             print('Обычная газировка')

# soda = Soda('apple')
# soda.show_my_drink()

# Task2
# class Nicola:
    
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def nicolai(self):
#         name1 = 'Николай'
#         if self.name == name1:
#             print(self.name)
#         else:
#             print(f'Я не {self.name}, а {name1}')

# person1 = Nicola('Максим', 33)
# person1.nicolai()
# person1.surname = 'Ivanov'


# class House:
#     def __init__(self, type_house, total_area, left_area, list_of_furniture):
#         self.type_house = type_house
#         self.total_area = total_area
#         self.left_area = left_area
#         self.list_of_furniture = list_of_furniture

#     def info(self):
#         print()


# class Furniture(House):
#     def __init__(self, type_house, total_area, left_area, name_of_furniture, furniture_square):
#         super().__init__(type_house, total_area, left_area)
#         self.name_of_furniture = name_of_furniture
#         self.furniture_square = furniture_square

#     def area(self):
#         self.total_area - self.furniture_square

# class Furniture:
#     def init(self,name_of_furniture,furniture_square):
#         self.name_of_furniture = name_of_furniture
#         self.furniture_square = furniture_square
#     def repr(self) -> str:
#         return f'{self.name_of_furniture},{self.furniture_square}'

# class House:
#     def init(self, type, area):
#         self.type = type
#         self.area = area
#         self.left_area = area
#         self.list_of_furniture = []
#     def add(self,classes):
#         if self.area > classes.furniture_square:
#             self.list_of_furniture.append(classes)
#             self.left_area -= classes.furniture_square
#         else: 
#             print('Площаль мебели больше площади дома')
    
#     def str(self):
#         return f'тип дома:{self.type}, площадь дома:{self.area}, оставшаяся площадь:{self.left_area}, список мебели: {self.list_of_furniture}'

# krovat = Furniture('bed',2)    
# bassein = Furniture('pool',100)
# house = House('kvartira',200)
# house.add(krovat)
# house.add(bassein)
# print(house)

# class Group:
#     def __init__(self, name, mentor, start_time, end_time, lang):
#         self.name = name
#         self.mentor = mentor
#         self.start_time = start_time
#         self.end_time = end_time
#         self.lang = lang
    
#     def add_student(self, student_list):
#         if type(student_list) is list:
#             student_list.append


# class Student:
#     def __init__(self, sum_, man, women):
#         self.sum_ = sum_
#         self.man = man
#         self.women = women

"""
Задача 1. Дана функция:
def say_hi():
    return 'python is good language'
print(say_hi())

Написать и применить к ней три декоратора:
Первый декоратор - для приведения всех символов к верхнему регистру
Второй декоратор - для разделения строки
Третий декоратор - для объединения в одно предложение
В результате должно получиться: "PYTHON IS GOOD LANGUAGE"
"""

# def upper(func):
#     def wrapper():
#         return func().upper()
#     return wrapper

# def split(func):
#     def wrapper():
#         return func().split()
#     return wrapper

# def join(func):
#     def wrapper():
#         return ' '.join(func())
#     return wrapper

# @join
# @split
# @upper
# def say_hi():
#     return 'python is good language'
# print(say_hi())

"""Задача 2. Калькулятор
Напишите программу с классом Math. Создайте два атрибута — a и b. 
Напишите методы addition — сложение, multiplication — умножение, division — деление, subtraction — вычитание. 
При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ."""


# class Math:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def add_(self):
#         return self.a + self.b

#     def multiplication(self):
#         return self.a * self.b

#     def division(self):
#         return self.a / self.b

#     def sucstraction(self):
#         return self.a - self.b

# x = Math(5, 6)
# print(x.add_())
# x.multiplication()
# x.division()
# x.sucstraction()
"""
Задача 3. Профиль 
Создайте класс профиля из соц сети. У профиля должен быть никнейм, эл. почта и возраст. 
Также создайте метод get_info, который выводит информацию о профиле в следующем виде: 
Nickname: girl_hunter 
Email: your_hero@gmail.com
Age: 12 y.o.
Затем объявите экземляр класса и вызовите метод.
"""

# class Profile:
#     def __init__(self, nickname, email, age):
#         self.nickname = nickname
#         self.email = email
#         self.age = age

#     def get_info(self):
#         print(f'Nickname: {self.nickname}\nEmail: {self.email}\nAge: {self.age}')

# person1 = Profile('boy', 'sadboy', 11)
# person1.get_info()

"""
Задача 4. Напишите программу с классом Car. Создайте конструктор класса Car. 
Создайте атрибуты класса Car — color (цвет), brand (тип), year (год). Напишите пять методов. 
Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен». 
Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен». 
Третий — присвоение автомобилю года выпуска. 
Четвертый метод — присвоение автомобилю бренда. 
Пятый — присвоение автомобилю цвета.
# """

# class Car:
#     def __init__(self, color, brand, year):
#         self.color = color
#         self.brand = brand
#         self.year = year

#     def car_on(self):
#         print('Автомобиль заведен')

#     def car_off(self):
#         print('Автомобиль заглушен')

#     def set_year(self, new_year):
#         self.year = new_year

#     def set_brand(self, new_brand):
#         self.brand = new_brand

#     def set_color(self, new_color):
#         self.color = new_color

# car1 = Car('blue', 'Toyota', 2020)
# car1.car_off()
# car1.set_year(2021)
# print(car1.year)
"""
Задача 5. Спортсмены
Создайте классы Footballer и Snowboarder с одинаковым методом skill_info. Для футболиста он должен печатать "Я могу забить штрафной с 30 метров", для сноубордиста "В прыжке я делаю разворот на 360 градусов".
Объявите для каждого из классов по экземпляру. Затем объявить функцию show_skills, которая будет принимать спортсмена и вызывать у него метод skill_info.
"""

# class Footballer:
#     def __init__(self):
#         pass

#     def skill_info(self):
#         print('Я могу забить штрафной с 30 метров')


# class Snowboarder:
#     def __init__(self):
#         pass

#     def skill_info(self):
#         print('В прыжке я делаю разворот на 360 градусов')


# person1 = Footballer()
# person2 = Snowboarder()

# def show_skills(func):
#     func.skill_info()

# show_skills(person1)
# show_skills(person2)