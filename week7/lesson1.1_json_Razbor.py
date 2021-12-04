import json


json_str = '{"a": [1, "a"], "b": [2, "b"]}'
# python_dict = {"a": [1, "a"], "b": [2, "b"]}
python_obj = json.loads(json_str)
print(python_obj)

python_obj = {1: 1, 2:2, 3:3}
json_obj = json.dumps(python_obj)
print(json_obj)

# print(type(json_str)) -> python str
# print(type(python_dict)) -> python dict

# file_ = open("main.json", 'w')
# json.dump() -> работает с файлом, записывает python объект в этот файл
# json.dump(python_dict, file_)

# file_.close()

# file_ = open("main.json", 'w')
# # json.load(file) -> работает с файлом, возвращает данные в виде питон объектов

# python_object = json.load(file_) # ->
# print(python_object)

# open(file, "w") -> json.dump()
# open(file, "r") -> json.load()


# "w"  -> запись с удалением
# "r"  -> только чтение
# "a"  -> только запись в конце файла
# "w+" -> сначала очищает файл, потом позволяет записывать и считывает данные
# "a+" -> позволяет записывать и считывать данные
# file_ = open("main.json", "r")
# json.load(file_)


# import json
# from os import utime
# with open("bd.json") as file:
#     python_bd = json.load(file)

# def exit():
#     confirmation = input("Вы хотите выйти (q): ").lower()
#     if confirmation == 'q':
#         return True

# def login(user = None):
#     if user is None:
#         user = input("Введите логин: \n")
#     if user in python_bd:
#         password = input("Введите пароль: \n")
#         if python_bd[user] == password:
#             print("Вы успешно зашли")
#         else:
#             print("Пароль не совпадает")
#             if exit(): return
#             login(user)
#     else:
#         print("Такого юзера нет")
#         if exit(): return
#         login()

# login()

# def register(name = None):
#     if name is None:
#         name = input("Введите имя: \n")
#     if name in python_bd:
#         print("Юзер с таким именем уже существует")
#         if exit(): return
#         register()

#     password = input("Введите пароль: \n")
#     password_confirm = input("Потвердите пароль: \n")
#     if password != password_confirm:
#         if exit(): return
#         register(name)
#     else:
#         python_bd[name] = password

#         with open("bd.json", "w") as file:
#             json.dump(python_bd, file)
#         # print(python_bd)
#         return

# register()
# def func(name = input("name: ")):
#     if name == "nastya":
#         func()
#     func()

# print('1')
# func()
# print('2')
# func()
# print('3')
# func()