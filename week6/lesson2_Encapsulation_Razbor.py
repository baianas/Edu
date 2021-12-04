#модификаторы:

# публичные - доступны в самом классе, в его дочерних классах и вне класса

# attr1, method1()

# защищенные - недоступны вне класса, но при этом доступны в самом классе, и в его дочерних классах

# _attr1, _method2()

# приватные - доступны только в самом классе

# __attr2, __method2()

# getter, setter

# setter - метод, устанавливающий значение
# getter - метод, получающий значение


# class Stabilizer:
#     __voltage = 220

#     def set_voltage(self, new_voltage):
#         if new_voltage > 300:
#             raise ValueError('Превышено максимальное значение')
#         self.__voltage = new_voltage

#     def get_voltage(self):
#         return self.__voltage

# stab1 = Stabilizer()
# stab1.set_voltage(230)
# stab1.get_voltage()


# class Stabilizer:
#     __voltage = 220

#     @property
#     def voltage(self):
#         return self.__voltage


#     @voltage.setter
#     def voltage(self, new_voltage):
#         if new_voltage > 300:
#             raise ValueError('Превышено максимальное значение')
#         self.__voltage = new_voltage

    

# stab1 = Stabilizer()
# stab1.voltage = 200
# stab1.voltage


# class A:
#     attr1 = 'a'
#     _attr2 = 'b'

# a1 = A()
# a1.attr1 #'a'
# a1._attr2 #'b' так возможно сделать, но нельзя


# def decorator(func):
#     def wrapper(x):
#         res = func(x)
#         return res
#     return wrapper

# @decorator
# def my_func(x):
#     return x *10

# print(my_func(10))

# def decorator(cls):
#     class NewClass:
#         def __init__(self) -> None:
#             pass

#     return NewClass


# @decorator
# class A:
#     pass