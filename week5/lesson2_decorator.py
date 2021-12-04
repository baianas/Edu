#декораторы

#функция - это объект

# a = 4 #int
# b = '123' #str
# c = [1, 2, 3] #list
# d = (1, 2, 3) #tuple

# def my_func():
#     pass

# my_func() #function 

#функцию можно присвоить переменной

# def func1():
#     print('Hello World')

# a = func1

# a()

#функцию можно передавать в качестве аргумента и возвращать в качестве результата 
#также внутри функции могут определяться локальные функции

# def func1():
#     pass

# def func2(function):
#     pass

# func2(func1)

# def func1():
#     def func2():
#         print('Hello world')
#     return func2

# func1()()

#декоратор (функция для функций) - функция, которая принимает функцию, наделяет её дополнительным функционалом, но при этом исходный код принятой функции не изменяется

# def decorator(function):
#     def wrapper():
#         import datetime
#         function()
#         print(f'Текущее время: {datetime.datetime.now()}')
#         print('Функция окончена')
#     return wrapper

# @decorator
# def func1():
#     print("A")
#func1 = decorator(func1)

    
# @decorator
# def func2():
#     print("B")
    
# @decorator
# def func3():
#     print("С")
   
#напсиать декоратор login, который будет записывать в файл, какая функция вызвана и во сколько и с какими аргументами. Применить его к 3 разным функциям

# def login(function):
#     def wrapper(*args, **kwargs):
#         import datetime
#         with open('log.txt', 'a') as file:
#             current = datetime.datetime.now().strftime('%d-%m-%Y %H:%M:%S')
#             result = function(*args, **kwargs)

#             file.write(f'Функция {function.__name__} вызвана {current}\n')
#             file.write('------------\n')
#         return result
#     return wrapper

# @login
# def func1():
#     print('Hello world')

# @login
# def func2(x, y):
#     print(x * y)

# @login
# def func3(list_):
#     print(sum(list_))
    
# func1()
# func2(10, 20)
# func3([1, 2, 3, 4])


# def func(*args, **kwargs):
#     #args -> (1, 2, 3)
#     #kwargs -> {'a':1, 'b': 2, 'c': 3}

# func(1, 2, 3, a = 1, b = 2, c = 3)

# def func(a, b, c):
#     pass

# func(1, 2, 3)
# func(a=1, b=2, c=3)
# func(1, 2, c=3)

# list1 = [1, 2, 3]
# tuple1 = (1, 2, 3)

# # func(*list1)
# # func(*tuple1)
# # func(1, 2, 3)

# dict1 = {'a': 1, 'b': 2, 'c': 3}
# func(**dict1)
# func(a=1, b=2, c=3)

# @login
# def multiply(x, y):
#     return x * y

# # multiply = login(multiply)
# # multiply = wrapper

# multiply(10, 10) #100


# Написать декоратор, который замеряет время выполнения функции в миллисекундах

# def timer(func):
#     def wrapper(*args, **kwargs):
#         import time
#         start = time.time()
#         result = func(*args, **kwargs)
#         end = time.time()
#         working_time = end - start
#         print(f'Время выполнения: {working_time *1000} миллисекунд')
#         return result
#     return wrapper
    
# @timer
# def func1():
#     print('Hello world')

# @timer
# def func2(x, y):
#     print(x * y)

# @timer
# def func3(list_):
#     print(sum(list_))

# func1()
# func2(10, 20)
# func3([1, 2, 3, 4])


# Написать декоратор, который замеряет среднее время выполнения функции в миллисекундах за n выполнений

def timer(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            import time
            total_time = 0
            for _ in range(n):
                start = time.time()
                result = func(*args, **kwargs)
                end = time.time()
                working_time = end - start
                total_time += working_time
            avg_time = total_time / n
            print(f'Время выполнения: {avg_time *1000} миллисекунд')
            return result
        return wrapper
    return decorator
    
@timer(100)
def func1():
    print('Hello world')

@timer(100)
def func2(x, y):
    print(x * y)

@timer(100)
def func3(list_):
    print(sum(list_))

func1()
func2(10, 20)
func3([1, 2, 3, 4])

# @classmethod
# @staticmethod
# @property
# @setter


# @login_required
# @action

