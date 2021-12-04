#Task1
# list_ = [i for i in range(1, 101)]
# print(list_)

#Task2
# list_ = [i for i in range(1, 50) if i % 2 != 0]
# print(list_)

#Task3
# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# int_list = [i for i in list_ if i % 2 == 0 and i > 0]
# print(int_list)

#Task4
# list_ = [i ** 2 for i in range(1, 26)]
# print(list_)

#Task5
# str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
# int_list = [int(i) for i in str_list]
# print(int_list)

#Task6
# list_ = [i ** 2 if i % 2 == 0 else  i for i in range(1, 11)]
# print(list_)

#Task7
# list_ = [True if i % 2 == 0 else False for i in range(1, 11)]
# print(list_)

#Task8
# list_name = ['paul', 'john', 'george', 'ringo', 'eric', 'patty', 'yoko', 'cynthia', 'linda', 'jude']
# new_list = ['shorter' if len(name) <= 4 else 'longer' for name in list_name]
# print(new_list)

#Task9
# dict_ = {num: num ** 2 for num in range(1, 11)}
# print(dict_)

#Task10
# n = int(input())
# dict_ = {i: i ** 2 for i in range(1, 501) if i % n== 0}
# print(dict_)

#Task11
# a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}
# dict_ = {k: list(range(1, v+1)) for k, v in a.items()}
# print(dict_)

#Task12
# dict_ = {'first': 1, 'second': 2, 'third': 3}
# a = {k: 'even' if v % 2 == 0 else 'odd' for k, v in dict_.items()}
# print(a)

#Task13
# string_ = 'In 1984 there were 13 instances of a protest with over 1000 people attending'
# list_ = [i for i in string_.split() if i.isdigit()]
# print(list_)

#Task14
# dict_ = {'Timur': {'history': 90, 'math': 95, 'literature': 91}, 
# 'Olga': {'history': 92, 'math': 96, 'literature': 81}, 
# 'Nik': {'history': 84, 'math': 85, 'literature': 87}}
# res = {name: subject for name, marks in dict_.items() for subject, score in marks.items() if score == max(marks.values())}
# print(res)

#Task15
# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# dict_ = {key: num for key, value in my_dict.items() for alpha, num in value.items()}
# print(dict_)

# dict_ = {} 
# for key, value in my_dict.items(): 
#  for alpha, num in value.items(): 
#    dict_[key] = num

# print(dict_)


#Extra-Task1
# list_ = [i / 2 for i in range(0, 11) if i % 2 == 0]
# print(list_)

#Extra-Task2
# dict_ = {55: 'ahrhb', 13: 'berger', 7: 'cthbrtbn'}
# b = {len(v): v if k % 2 == 0 else len(v) ** 3 for k, v in dict_.items()}
# print(b)

#Extra-Task3
