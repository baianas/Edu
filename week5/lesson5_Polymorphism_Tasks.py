#Task1
# a = '12342342345' 
# b = [1,['a',5,6],2,3,4,5] 
# c = {1:'a', 2: {'a': 1, 'b': 2}, 3:'c'}

# d = [a, b, c]
# for i in d:
#     print(len(i))


#Task2
# class Dog:
#     def voice(self):
#         print('Гав')
        
# class Cat:
#     def voice(self):
#         print('Мяу')
        
    
# barsik = Cat()
# rex = Dog()

# def to_pet(animal):
#     animal.voice()

# to_pet(barsik) 
# to_pet(rex)


#Task3
# class Person:
#     def __init__(self, name, last_name):
#         self.name = name
#         self.last_name = last_name
        
#     def get_info(self):
#         return f'Привет, меня зовут {self.name} {self.last_name}'
    
# class Employee(Person):
#     def __init__(self, name, last_name, work, status):
#         super().__init__(name, last_name)
#         self.work = work
#         self.status = status
        
#     def get_info(self):
#         return super().get_info() + f', я работаю в компании {self.work} на должности {self.status}'
    
# class Student(Person):
#     def __init__(self, name, last_name, university, course):
#         super().__init__(name, last_name)
#         self.university = university
#         self.course = course
        
#     def get_info(self):
#         return super().get_info() + f', я учусь в {self.university} на {self.course} курсе'
        
# def get_human_info(person):
#     print(person.get_info())
        
# employee = Employee('Иван', 'Петров', 'Рога и Копыта', 'директор')
# student = Student('Иван', 'Петров', 'КГТУ', 3)
# person = Person('Иван', 'Иванов')

# get_human_info(employee) 
# get_human_info(student) 
# get_human_info(person)


#Task4
# from abc import ABC, abstractmethod
# from math import pow, pi
# class Shape(ABC):
#     @abstractmethod
#     def get_area():
#         raise NotImplementedError

# class Triangle(Shape):
#     def __init__(self, base, height):
#         self.base = base
#         self.height = height
#     def get_area(self):
#         return (self.base * self.height)/2
       
# class Square(Shape):
#     def __init__(self, length):
#         self.length = length

#     def get_area(self):
#         return (self.length ** 2)

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius

#     def get_area(self):
#         return pow(self.radius, 2) * pi

# triangle = Triangle(123, 453)
# square = Square(564)
# circle = Circle(456)
# print(triangle.get_area())
# print(square.get_area())
# print(circle.get_area())


#Task5
