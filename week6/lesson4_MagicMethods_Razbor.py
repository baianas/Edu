# Магические методы нужны для того, чтобы созданные нами объекты могли работать со встроенными функциями и операциями

# арифметические операции:
"""
+  -> __add__(self, other):
self + other

__radd__(self, other):
other + self

-  -> __sub__(self, other):
self - other
__rsub__(self, other):
other - self

*   -> __mul__(self, other):
/   -> __truediv__(self, other):
//  -> __floordiv__(self, other):
%   ->__mod__(self, other):
**  ->__pow(self, other):
"""
# class Balance:
#     def __init__(self, value) -> None:
#         self.value = value

#     def __add__(self, other):
#         return self.value + other.value

# balance1 = Balance(100)
# balance2 = Balance(200)

# print(balance1 + balance2)

# операции сравнения

# == -> __eq__(self, other)
# != -> __ne__(self, other)
# >  -> __gt__(self, other)
# <  -> __lt__(self, other)
# >= -> __ge__(self, other)
# <= -> __le__(self, other)

# a = 5
# b = 4

# a>b #True

# class Forbes:
#     def __init__(self, name, capital) -> None:
#         self.name = name
#         self.capital = capital

#     def __gt__(self, other):
#         return self.capital > other.capital

#     def __lt__(self, other):
#         return self.capital < other.capital

#     def __eq__(self, other):
#         return self.capital == other.capital

#     def __ne__(self, other):
#         return self.capital != other.capital

#     def __ge__(self, other):
#         return self.capital >= other.capital

#     def __le__(self, other):
#         return self.capital >= other.capital

# mark = Forbes('Mark Zuckerberg', 200)
# jeff = Forbes('Jeff Bezos', 240)

# print(mark > jeff)

# приведение типа

# str(obj) -> obj.__str__()
# int(obj) -> obj.__int__()
# bool(obj)-> obj.__bool__()


# a = [1, 2, 3, 4]
# b = {'a': 1, 'b': 2}

# доступ к элементам
# a[0]   -> a.__getitem__(0)
# b['a'] -> b.__getitem__('a')

# замена элементов
# a[0] = 5    -> a.__setitem__(0, 5)
# b['a'] = 22 -> b.__setitem__('a', 22)

#удаление элементов
# del a[0]    -> a.__delitem__(0)
# del b['b']  -> b.__delitem__('b')

# нахождение длины

# len(a)   -> a.__len__()
# len(b)   -> b.__len__()

# проверка на вхождение

# value in a   -> a.__contains__(value)
# key in b     -> b.__contains__(key)

# итерация
# for x in a   -> a.__iter__()
# iter(a)      -> a.__iter__()

# reversed(реверсирование)

# reversed(a)   -> a.__reversed__()

# вызов встроенных фцнкций
# print(obj)   -> obj.__str__()
# repr(obj)    -> obj.__repr__()
# round(obj)   -> obj.__round__()

# обращение к атрибутам

# class MyClass():
#     attr1 = 'a'


# obj1 = MyClass()

# obj1.attr1   -> obj1.__getattribute__('attr1')
# obj1.attr1 = 'new_alue'  -> obj1.__setattr__('attr1', 'new_value')
# del obj1.attr1   -> obj1.__delattr__('attr1')


# setattr('obj1', 'attr1', 'new_value'), delattr(obj1, 'attr1'), getattr(obj1, 'attr1'), hasattr(obj1, 'attr1')


# class A:
#     attr1 = 'a'


# a1 = A()
# # a1.attr2 = 100
# setattr(a1, 'attr2', 100)
# print(getattr(a1, 'attr2'))  #100
# print(hasattr(a1, 'attr2'))


# a2 = A()
# print(getattr(a2, "attr2"))
# print(hasattr(a2, 'attr2'))