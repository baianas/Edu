# Dictionary Comprehensions
# names = ['Bruce', 'Clark', 'Peter', 'Logan', 'Wade']
# heros = ['Batman', 'Superman', 'Spiderman', 'Wolverine', 'Deadpool']
# print(list(zip(names, heros)))

# # I want a dict{'name': 'hero'} for each name,hero in zip(names, heros)
# my_dict = {}
# for name, hero in zip(names, heros):
#     my_dict[name] = hero
# print(my_dict)

# my_dict = {name: hero for name, hero in zip(names, heros)}
# print(my_dict)



"""
Дан словарь a в котором значениями являются целые числа. 
Пройдитесь по элементам и запишите в dict_ значения на список чисел от 1 до числа, которое является значением
"""


# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
 
#  -> 
 
# {'a': [1], 'b': [1, 2, 3, 4, 5], 'c': [1, 2, 3, 4], 'd': [1, 2, 3]}
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1, v+1)) for k, v in a}
# print(dict_)

# a = {'a': 1, 'b': 5, 'c': 4, 'a': 3}
# dict_ = {alpha: num ** 2 for alpha, num in a.items()}
# print(dict_)

# my_dict = {[1, 2, 3, 4, 5]: ['a', 'b', 'c', 'd', 'e']}
# new_my_dict = {num: alpha for num, alpha in my_dict.items()}
# print(new_my_dict)
# a1 = {1: 'a', 2: 'b'}


