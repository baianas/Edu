#наследование

# class A:
#     #class attributes
#     attr1 = 'a'

#     def __init__(self, attr2):
#         #instance attributes
#         self.attr2 = attr2

#     def method1(self):
#         print('hello!')

#наследование, инкапсуляция, полиморфизм

#наследование - произведение одних классов от других
#родительский класс, суперкласс
# class A:
#     attr1 = 'a'

#     def method1(self):
#         print('Hello!')

# #дочерний (производный) класс, подкласс
# class B(A):
#     pass

# b1 = B()
# b1.attr1
# b1.method1()

# print(issubclass(B, A)) #True

# isinstance(b1, B) #True
# isinstance(b1, A) #True

# print(type(b1)) #'main.B'

#дочерний класс может переопределять значения атрибутов или поведение методов родителя

# class A:
#     attr1 = 'a'

#     def method1(self):
#         print('AAA')

# class B(A):
#     attr1 = 'b'

#     def method1(self):
#         print('BBB')

# b1 = B()
# b1.attr1 #'b'
# b1.method1() #'BBB'

#дочерние класс могут дополнять поведение родителей

# super() - функция для обращения к родительскому классу

# class A:
#     attr1 = 'a'

#     def method1(self):
#         print('AAA')

#     def method2(self):
#         return self.attr1.upper()


# class B(A):
#     def method1(self):
#         super().method1()
#         print('BBB')

#     def method2(self):
#         value = super().method2()
#         my_value = value + 'B'
#         return my_value

# b1 = B()
# b1.method2() #'AB'

# class Animal:
#     pass

# class Mammal(Animal):
#     feeding = 'Milk'

# class Cat(Mammal):
#     pass

# class Wildcat(Cat):
#     pass

# class Homecat(Cat):
#     pass

# class A:
#     attr1 = 'a'

# class B(A):
#     attr1 = 'b'

# class C(A):
#     attr1 = 'c'

# class D(C):
#     attr1 = 'd'

# d1 = D()
# d1.attr1 #'d;

# D -> C -> B -> A -> object

# ассоциация - связь объектов разных классов

# class Engine:
#     def __init__(self, fuel, volume, power):
#         self.fuel = fuel
#         self.volume = volume
#         self.power = power

# v8 = Engine('gasoline', 5, 350)
# v6 = Engine('diesel', 3, 200)

# class Car:
#     def __init__(self, model: str, year: int, color: str, engine: Engine):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.engine = engine

# car1 = Car('Toyota Land Cruiser', 2009, 'black', v8)

# class Car:
#     def __init__(self, model: str, year: int, color: str, fuel, volume, power):
#         self.model = model
#         self.year = year
#         self.color = color
#         self.engine = Engine(fuel, volume, power)

# car1 = Car('Toyota Land Cruiser', 2009, 'black', 'diesel', 4.2, 300)

# car1.engine.volume


# class Category:
#     def __init__(self, name, id):
#         self.name = name
#         self.id = id

# cat1 = Category('Электроника', 1)
# cat2 = Category('Техника для кухни', 2)

# class Product:
#     def __init__(self, name, description, price, category):
#         self.name = name 
#         self.description = description
#         self.price = price
#         self.category = category

# p1 = Product('Apple Iphone 12', '....', 100000, cat1)
# p2 = Product('Блендер Bosch M-290', '.....', 4500, cat2)

# class User:
#     def __init__(self, email, addres, phone_number):
#         self.email = email
#         self.addres = addres
#         self.phone_number = phone_number

# user1 = User('nik.001@gmail.com', 'Токтогула, 197', +9960000000000000)

# class Order:
#     def __init__(self, id, user, date):
#         self.id = id
#         self.user = user
#         self.date = date
        
# order1 = Order(1, user1, '10-11-2021 18:58')

# class OrderItem:
#     def __init__(self, order_id, product, quantity):
#         self.order_id = order_id
#         self.product = product
#         self.quantity = quantity

# order_item1 = OrderItem(order1.id, p1, 2)
# order_item2 = OrderItem(order1.id, p2, 4)

# class A:
#     instance_count = 0

#     def __new__(cls):
#         cls.instance_count += 1
#         return super().__new__(cls)

# a1 = A()
# a2 = A()
# print(A.instance_count)

class A:
    attr1 = [1, 2, 3]

    def method1(self, value):
        self.attr1.append(value)

a1 = A()
a2 = A()
a1.method1(4)
print(a2.attr1)

def func(list_=[]):
    ...
    