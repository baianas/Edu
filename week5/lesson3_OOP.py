#ООП (Объектно - ориентиррванное программирование) - подход (парадигма), в котором части программы выражаются в виде объектов

# Объекты описываются классами

# class Classname:
#     pass

# a = 4 #int
# b = '3' #str
# c = [1, 2, 3] #list

# class Phone:
#     model = 'Xiaomi Mi 11'
#     size = 5.5
#     color = 'black'
#     ram = 6

# phone1 = Phone()
# phone2 = Phone()

# class Phone:
#     #атрибуты класса
#     operating_system = 'Android'
#     def __init__(self, model, size, color, ram, memory):
#         #атрибуты экземпляра класса
#         self.model = model
#         self.size = size
#         self.color = color
#         self.ram = ram
#         self.memory = memory

#     def call(self):
#         pass

#     def play_video(self):
#         pass
        
# phone1 = Phone('Samsung Galaxy S21', 5.54, 'black', 8, 512)
# # phone1 = Phone.__new__()
# # phone1.__init__('Xiaomi Mi 11', 5.5, 'space blue', 6, 1024)

# phone2 = Phone('Xiaomi Mi 11', 5.5, 'space blue', 6, 1024)

# print(phone1)


# class Human:
#     def __init__(self, name, last_name, date_of_birth, inn, phon_number, addres, weight, height, hair_color):
#         pass


# class Employee:
#     def __init__(self, name, last_name, date_of_birth):
#         pass
    

# class User:
#     pass

# class Client:
#     def __init__(self, name, addres, phone_number):
#         pass
    

# class Patient:
#     def __init__(self, name, last_name, age, date_of_birth, weight, height):
#         pass


# class Phone:
#     pass

# phone1 = Phone()

# class Car:
#     def __init__(self, model, year, volume, color, fuel):
#             self.model = model
#             self.year = year
#             self.volume = volume
#             self.color = color
#             self. fuel = fuel

#     def __str__(self) -> str:
#         return f'{self.model} {self.year} {self.color}'
        
# car1 = Car('Toyota Camry', 2015, 2.5, 'white', 'gasoline')
# car2 = Car('Honda Accord', 2012, 3.5, 'black', 'gasoline')

# print(car1)
# print(car2)

# a = '3'

# b = str('3')

# b.upper()

# class str:
#     def __init__(self, value):
#         self.value = value

#     def upper(self):
#         ...

#     def lower(self):
#         ...

# a = 1

# a = int('1')

# class A:

#     attr1 = 'a'

#     def __init__(self, attr2):
#         self.attr2 = attr2

# a1 = A(10)
# a2 = A(20)

# a1.attr1 #'a'
# a2.attr1 #'a'

# a1.attr1 = 'b'

# a1.attr2 #10
# a2.attr2 #20

# a2.attr1 #'a'


# class Car:
#     def __init__(self, model: str, volume: float, color: str) -> None:
#         pass

# from dataclasses import dataclass

# @dataclass
# class Phone:
#     model: str
#     year: int
#     ram: int
#     color: str
#     os: str


# phone1 = Phone('Apple Iphone 13', 2021, 8, 'gold', 'IOS')


#наследование 

# наследование - процесс, когда из одного класса происходит другой

#родительский (базовый) класс
#parent(base, inherited) class
# class A:
#     attr1 = 'a'

#     def method1(self):
#         print("Hello world")

# дочерний (производный) класс
#child (derived) class
# class B(A):
#     pass

# b1 = B()
# b1.attr1
# b1.method1()

#дочерний класс может определять свои свойства и методы

# class A:
#     attr1 = 'a'

# class B(A):
#     attr2 = 'b'
#     attr3 = 'c'

# b1 = B()
# b1.attr1
# b1.attr2
# b1.attr3

#дочерний класс может переопределять свойства родителя, дополнять методы родителя

# class A:
#     attr1 = 'a'
#     attr2 = 'b'

# class B(A):
#     attr3 = 'new'
#     attr2 = 'value'


# b1 = B()
# b1.attr2 #'value'

#переопределение
class A:
    def method(self):
        print('Hellooo!!!!')

class B(A):
    def method(self):
        super().method()
        print('BBB')

b1 = B()
b1.method()

