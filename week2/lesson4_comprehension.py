# comprehension

# исрользуется, когда необходимо обойти последовательность
# (строка, спсикок, кортеж, словарь, range), 
# сделать определенное действие и результат сохранить в новый список

# a = [1, 2, 3, 4, 5, 6, 7, 8]
# a = range(1, 9)
# a = (1, 2, 3, 4, 5, 6, 7, 8)
# [10, 20, 30, 40, 50, 60, 70, 80]
# res = []
# for i in a:
#     res.append(i * 10)
# print((res))

# [действие(элемент) for элемент in последовательность]

# res = [i * 10 for i in a]
# print(res)

#фильтровать элементы последоветовательности в новый

# list1 = [20, 45, 21, 34, 56, 21, 34, 31, 48, 19]

# [45, 21, 21, 48]

# new_list = []
# for i in list1:
#     if i % 3 == 0:
#         new_list.append(i)
# print((new_list))

# [действие(элемент) for элемент in последовательность if условие]

# new_list = [i for i in list1 if i % 3 == 0]
# print(new_list)

# a = [-10, 29, 0, 21, -2, 94, -21, 101, -99]

# ['-', '+', '+', '+', '-', '+', '-', '+', '-']

# [действие1(элемент)  if условие else действие2(элемент) for элемент in последовательность]

# new_list = ['+' if i >= 0 else '-' for i in a]
# print(new_list)

#dict comprehension

# a = {'a': '1', 'b': '2', 'c': '3'}
# b = {'a': 1, 'b': 20, 'c': 30}

# b = {}
# for k, v in a.items():
#     b[k] = int(v) *10

# b = {k: int(v) * 10 for k, v in a.items()}
# print(b)

# a = {'a': 10, 'b': -2, 'c': 2, 'd': -5}
# res #{'a': 10, 'c': 2}

# res = {k: v for k, v in a.items() if v >= 0} 

# a = {'Milk': 48, 'Eggs': 99, 'Meat': 500, 'Sugar': 48, 'Oil': 160}
#Если цена товара менньше 100, то нужно снизить на 5%, если больше, то на 10%. Округлить результат до двух знаков

# res = {k: round(v * 0.9, 2) if v > 100 else round(v * 0.95, 2) for k, v in a.items()}
# print(res)

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# [[10, 20, 30], [40, 50, 60], [70, 80, 90]]

# new = []
# for item in list1:
#     inner_list = []
#     for num in item:
#         inner_list.append(num * 10)
#     new.append(inner_list)

# new = [[num * 10 for num in item] for item in list1]

# list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for item in list1:
#     for num in item:
#         new.append(num * 10)

# new  = [num * 10 for item in list1 for num in item]
# print(new)

# a = {
#     'Timur': {'history': 92,
#     'math': 96, 'literature': 88},
#     'Olga': {'history': 82,
#     'math': 76, 'literature': 98},
#     'Nik' : {'history': 90,
#     'math': 88, 'literature': 88}
# }
# # # res = {'history': 82,

# res = {name: subject for name, marks in a.items() for subject, score in marks.items() if score == max(marks.values())}
# print(res)

# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# res = {name: subject for name, marks in dict_.items() for subject, score in marks.items() if score == max(marks.values())}
# print(res)

#Task15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: num for key, value in my_dict.items() for alpha, num in value.items()}
# print(dict_)