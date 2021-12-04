# class A:
#     def method(self):
#         print('A')


# class B:
#     def method(self):
#         print('B')

# class C(A, B):
#     def method(self):
#         super().method()
#         print('C')

# c1 = C()
# c1.method()

# # [C, A, B, object]


# class A:
#     pass

# class B(A):
#     pass

# class B(A):
#     pass

# class D(B, C):
#     pass

# [D, B, C, A, object]

# class CraneMixin:
#     def lift(self):
#         print('Поднимаю тяжести')


# class Truck:
#     pass


# class Manipulator(CraneMixin, Truck):
#     pass


# class Train:
#     pass


# class CargoTrain(CraneMixin, Train):
#     pass


# class Ship:
#     pass


# Абстрактный класс - класс без явной реализации хотя бы одного метода

# class Animal:
#     def walk(self):
#         pass


# class Snake(Animal):
#     def bite(self):
#         ...

#     def walk(self):
#         pass


# class Animal:
#     def eat(self):
#         raise NotImplementedError


# class Cat(Animal):
#     pass


# cat1 = Cat()
# cat1.eat()


# from abc import ABC, abstractmethod


# class Animal(ABC):

#     @abstractmethod
#     def eat(self):
#         pass


# class Cat(Animal):
#     def eat(self):
#         print('Я питаюсь мясом и молоком')

# cat1 = Cat()
# cat1.eat()


class Square:
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side ** 2

class Triangle:
    def __init__(self, base, height) -> None:
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.height * self.base

class Pyramid(Triangle, Square):
    def get_volume(self):
        from math import sqrt
        pyramid_height = sqrt(self.height ** 2 - (self.base / 2)**2)
        volume = self.base ** 2 * pyramid_height / 3
        return volume

a = Square(5)
b = Triangle(2, 3)
c = Pyramid(2, 3)
print(c.get_volume())