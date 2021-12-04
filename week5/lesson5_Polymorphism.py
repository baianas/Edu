#полиморфизм - возможность функции работать с объектами разных типов, при условии того, что объект поддерживает операцию (объект обладает нужным методом)

# a = 1
# b = 2

# a + b #3

# str1 = '1'
# str2 = '2'
# str1 + str2 #'12'
# str1.__add__(str2)

# a1 = [1, 2, 3]
# a2 = [4, 5, 6]

# a1 + a2 #[1, 2, 3, 4, 5, 6]


# class A:
#     def __init__(self, attr1):
#         self.attr1 = attr1

#     def __add__(self, other):
#         return self.attr1 + other.attr1

# a1 = A(10)
# a2 = A(20)

# print(a1 + a2)


# class A:
#     def __init__(self, value):
#         self.value = value

# a1 = A(10)
# a2 = A('20')
# a3 = A([1, 2, 3])
# a4 = A({'a':1, 'b': 2})

# def summarize(x, y):
#     print(x + y)


# summarize(10, 20)
# summarize('1', '2')
# summarize([1, 2], [3, 4])


# class object:
#     def __str__(self) -> str:
#         pass

# class A(object):
#     pass

# class int(object):
#     pass

# len(sequence)

# a1 = 'string'
# a2 = [1, 2, 3]
# a3 = (1, 2, 3)
# a4 = {'a':1, 'b': 2}

# len(a1) #a1.__len__()

# def len(obj):
#     if hasattr(obj, '__len__'):
#         return obj.__len__()
#     raise TypeError('....')


# class Office:
#     def __init__(self, employees):
#         self.employees = employees
    
#     def __len__(self):
#         return len(self.employees)

# office1 = Office(['Alibek', 'Janyl', 'Ermek', 'Janybek', 'Inna'])

# print(len(office1))

# class Square:
#     def __init__(self, side):
#         self.side = side

#     def area(self):
#         return self.side ** 2

# sq1 = Square(10)

# class Circle:
#     def __init__(self, radius):
#         self.radius= radius

#     def area(self):
#         from math import pi
#         return  pi * (self.radius ** 2)

# circle1 = Circle(10)

# class Triangle:
#     def __init__(self, a, b, c):
#         self.a =a 
#         self.b=b
#         self.c=c

#     def perimeter(self):
#         return self.a + self.b + self.c

# triangle1 = Triangle(10, 14, 13)

# def get_shape_area(shape):
#     shape.area()

# get_shape_area(sq1)
# get_shape_area(circle1)
# get_shape_area(triangle1)

# def write_to_file(filename, format):
#     if format == 'json':
#         ...
#     elif format == 'csv':
#         ...

# class JSONWriter:
#     def write():
#         pass

# class CSV:
#     def write():
#         pass