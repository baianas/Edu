# Есть 3 типа методов:

# 1. Методы экземпляра класса(instance methods)

# Изменяют состояние объекта (изменять атрибуты объекта) и класса

class A:
    attr1 = 'a'

    def __init__(self, attr2) -> None:
        self.attr2 = attr2

    def set_attr1(self, value):
        self.attr1 = value

    def set_attr2(self, value):
        self.__class__.attr2  = value

a1 = A(10)
a2 = A(20)

# a1.set_attr1(11)
# print(a1.attr1)
# print(a2.attr1)

a1.set_attr2(30)
print(a1.attr2)
print(a2.attr2)

# 2. Методы класса (class methods)

# изменяют только состояние класса, но не его объектов

# class A:
#     attr1 = 'a'

#     def __init__(self, attr2) -> None:
#         self.attr2 = attr2

#     def set_attr1(self, value):
#         self.attr1 = value

#     @classmethod
#     def set_attr2(cls, value):
#         cls.attr2 = value


def generate_vin():
    import random
    code  = random.randrange(1, 1000)
    return code


class Car:
    produced = []

    def __init__(self, vin_code):
        self.vin = vin_code

    @classmethod
    def create(cls):
        vin_code = generate_vin()
        cls.produced.append(vin_code)
        return cls(vin_code)
# 3. Статистические методы (static methods)

# - это функция, которая помещена внутрь класса для группировки логики. Не имеет доступа ни к классу, ни к его объектам


def celsius_to_fahrenheit(temperature):
    pass


def fahrenheits_to_celsius(temperature):
    pass

def meter_to_yard(distance):
    pass

def kg_to_pound(weight):
    pass


class Converter:
    @staticmethod
    def celsius_to_fahrenheit(temperature):
        pass

    @staticmethod
    def fahrenheits_to_celsius(temperature):
        pass

    @staticmethod
    def meter_to_yard(distance):
        pass

    @staticmethod
    def kg_to_pound(weight):
        pass
