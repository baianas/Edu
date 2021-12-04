# Task1
# def call_function(func):
#     def wrapper():
#         print(f"Вызываю функцию {func.__name__}")
#         func()
#         print(f"Вызов функции {func.__name__} прошёл успешно")
#     return wrapper()
    
    
# @call_function
# def first():
#     print("hello world")
#     return "hello world"

# first

#Task2
# def func_start_time(func):
#     from datetime import datetime
#     def wrapper():
#         print(f'Функция запущена {datetime.now()}')
#         func()
#     return wrapper
    
    
# @func_start_time
# def func():
#     print('Hello world')
# func()

#Task3
# def make_bold(func):
#     def wrapper():
#         return(f'<b>{func()}</b>')
#     return wrapper


# def make_italic(func):
#     def wrapper():
#         return(f'<i>{func()}</i>')
#     return wrapper


# def make_underline(func):
#     def wrapper():
#         return(f'<u>{func()}</u>')
#     return wrapper
    

# @make_bold
# @make_italic
# @make_underline
# def hello():
#     return 'Hello world'

# print(hello())

# Task4
# def benchmark(func):
#     def wrapper():
#         import time
#         start_time = time.time()
#         func()
#         return(f'Время выполнения: {time.time() - start_time}')
#     return wrapper
    
# @benchmark 
# def fetch_webpage(): 
#     import requests 
#     webpage = requests.get('https://google.com')

# print(fetch_webpage())


#Task5
# users = {'jaanger': '123312', 'vlad': '46456', 'nazar': '456132', 'tima': '456123'}


# def validate_password(func):
#     def wrapper(username, password):
#         if username not in users.keys():
#             print('Username is not defined')
#         else:
#             if password not in users.values():
#                 print('Password is invalid')
#             else:
#                 func(username, password)
#     return wrapper
    
# @validate_password
# def login(username, password):
#         print(f'Welcome, {username}')

# login('jaanger', '123312')


#Task8
# name_format = ([('Leo', 'Nimoy', 40, 'M'),
#               ('Carrie', 'Fisher', 35, 'F'),
#               ('Harrison', 'Ford', 38, 'M')])

# def sort_names(func):
#     def wrapper(list_):
#         list_ = sorted(list_, key=lambda x: x[2])
#         result = func(list_)
#         return result
#     return wrapper
            

# @sort_names
# def prefix_name(list_:list):
#     list_of_names = []
#     for i in list_:
#         if i[-1] == 'M':
#             names = "Mr." + ' ' + i[0] + ' ' + i[1]
#             list_of_names.append(names)
#         else:
#             names = "Ms." + ' ' + i[0] + ' ' + i[1]
#             list_of_names.append(names)
#     return list_of_names

# print(prefix_name(name_format))