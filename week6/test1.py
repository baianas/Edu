"""
1) Напишите декоратор, который печатает перед вызовом полученной функции строку: "Вызываю функцию <имя_функции>". Затем следует вызов функции. После вызова функции должна печататься строка: "Вызов функции <имя_функции> прошёл успешно"
"""
# def decorator(func):
#     print(f'Вызываю функцию {func.__name__}')
#     func()
#     print(f'Вызов функции {func.__name__} прошёл успешно')

# @decorator
# def func1():
#     print('Меня вызвали')

# func1
"""
2) Создайте класс Circle, с переменными класса задающие по умолчанию цвет круга - синий, и число Пи(3.14). Экземпляры класса Circle в свою очередь должны иметь обязательный аттрибут - радиус. Также класс должен иметь метод расчета площади круга. Создайте экземпляр класса, переопределите цвет экземпляра и расчитайте площадь фигуры.
"""

# class Circle:
#     color = 'синий'
#     pi = 3.14
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         print(self.radius **2)

# krug = Circle(5)
# krug.color = 'red'
# krug.area()
# print(krug.color)


"""
3) Создайте класс телефонной книги. У контактов должны быть имена и фамилии и номер телефона. Также создайте метод get_info, который выводит информацию о контакте в следующем виде: "Контакт: Иван Петров, телефон: +996555777888".
Затем объявите экземляр класса и вызовите метод.
"""

# class Numbook:
#     def __init__(self, name, surname, number):
#         self.name = name
#         self.surname = surname
#         self.number = number

#     def get_info(self):
#         print(f'Контакт: {self.name} {self.surname}, телефон: +{self.number}')

# person1 = Numbook('Shrek', 'Bolotov', 996555777888)
# person1.get_info()

"""
4) Создайте класс Person который будет описывать человека, а точнее его имя и возраст. Создайте метод display(), который будет выводит данные об этом человеке.
Создайте второй класс Student, который будет наследоваться от класса Person, он должен принимать все атрибуты, которые были определены в родительском классе и добавьте еще один атрибут, который будет описывать направление студента. Создайте метод display_student(), который будет выводить данные об этом студенте.
Объявите экземпляр класса Student, и выведите данные о нём, как о человеке, затем как о студенте.
"""

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print(f'name: {self.name}, age: {self.age}')


# class Student(Person):
#     def __init__(self, name, age, faculty):
#         super().__init__(name, age)
#         self.faculty = faculty

#     def display_student(self):
#         print(f'name: {self.name}, age: {self.age}, faculty: {self.faculty}')

# person1 = Student('Osel', 11, 'Drakonoborez')
# person1.display_student()

"""
5) Создайте классы Dog и Cat с одинаковым методом voice. Для собак он должен печатать "Гав", для кошек "Мяу".
Объявите для каждого из классов по экземпляру. Затем объявить функцию to_pet(), которая будет принимать животное и вызывать у него метод voice()
"""

# class Dog:
#     def voice(self):
#         print('Гав')


# class Cat:
#     def voice(self):
#         print('Мяу')

# rex = Dog()
# barsik = Cat()

# def to_pet(animal):
#     animal.voice()

# to_pet(rex)
# to_pet(barsik)

# def func(x):
#     return x * 2
# print(func(func("string")))
# print(func(3) * func(func(4)))

# def func(x):
#     return x
# def func(x):
#     return 2 * x
# def func(x):
#     return 3 * x
# print(func(5))

# class Parent:
#     x = 1
#     y = 2

# class Child(Parent):
#     x =111
#     y = 222

#     def mix(self):
#         return Parent.y

# c = Child()
# print(c.mix())

def decorator(func):
    def wrapper():
      print(f'Вызываю функцию {func.__name__}')
      func()
      print(f'Вызов функции {func.__name__} прошёл успешно')
    return wrapper

@decorator
def func1():
    print('Меня вызвали')

func1()