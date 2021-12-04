# x = int(input())
# y = int(input())
# # a = x // y
# # b = x % y
# c = x % y
# if c == 0:
#     print('output: x делится на y')
# else:
#     print('output: x не делится на y')
# print('Частное: ', x // y)
# if x % y:
#     print('Остаток: ', x % y)
# else:
#     print()

# # Task2
# x = int(input())
# y = int(input())
# c = x % y
# if c == 0:
#     print(x делится на y')
# else:
#     print('x не делится на y')
# print('Частное: ', x // y)
# if x % y:
#     print('Остаток:', x % y)


# Task9
# year = int(input())
# if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
#     print('YES')
# else:
#     print('NO')

# count = 0
# number = int(input())
# if type(number) == int():
#    count = number
# print(count)
   

# name_of_friends = ['Asan', 'Uson', 'Azamat', 'Vanya', 'Vasya']
# for i in name_of_friends:
#     print(i)

# name_of_list = ['Helloworld']
# a1 = int(len(name_of_list / 2))
# a = name_of_list[0][:int(a)]
# b = name_of_list[0][5:]
# print(a)
# print(b)

# name_of_list = ['Helloworld']
# a = len(name_of_list[0]) / 2

# print(a)

# count = int(0)
# number = int(input())
# if type(number) == int():
#     count = int(number)
# else:
#    print('aaa')
# print(count)

# list1 = ['tim', 'john', 'jack']
# for name in list1:
#     print(name.capitalize())

# name_of_list = ['Helloworld!']
# string = name_of_list[0]
# new_list = []
# lenght = len(string)
# mid = lenght // 2
# if lenght % 2 == 0:
#     mid += 1
# f_part = string[:mid]
# s_part = string[mid:]
# new_list.extend(list(s_part))
# new_list.extend(list(f_part))
# print(new_list)


# list_ = ['privet', 'mir']
# new_list = list_[::-1]
# print(new_list)
    
# suitcase = []
# suitcase.append('футболка')
# suitcase.append('шорты')
# suitcase.append('сланцы')
# suitcase.append('очки')
# suitcase.append('кепка')
# suitcase.pop()
# suitcase.insert(0, 'панама')
# print(suitcase)

# list_ = [1, 2, 3, 4, 5]
# new_list = str(list_)[:].replace(", ", "' '")
# print(new_list)

# list_ = [1, 2, 3, 4, 5]
# new_list = (list_(str[:]))
# print(new_list)

# a = {'a', 123, 'MAKERS', True}
# b = {'b', 456, 'Bootcamp', False}
# a.update(b)
# print(a)

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert & kail:
#     print('kail')
# if robert & merri:
#     print('merri')

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert & kail:
#     print('kailmerri')

# robert = {5, 7, 11, 10, 28}
# kail = {1, 5, 14, 8, 22}
# merri = {19, 20, 3, 11, 10}
# if robert & kail and robert & merri:
#     print('kail merri')
# elif robert & kail:
#     print('kail')
# elif robert & merri:
#     print('merri')


# tilek = {'Dodo', 'ImperiaPizza', 'FreshBox'}
# timur = {'OchakKebab', 'FreshBox'}
# alexander = {'FreshBox', 'KFC'}
# elina = {'Dodo', 'ImperiaPizza', 'FreshBox', 'KFC'}
# print(tilek & timur & alexander & elina)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for i in list_:
#    new_list.append(str(i))
# print(new_list)

# list_ = [1, 2, 3, 4, 5]
# new_list = []
# for a in list_:
#     if a // 2 == 0:
#        new_list.append('четное')
#     else:
#       new_list.append('нечетное')
# print(new_list)

# list_ = range(20)
# print(list(list_))

#Task13
# list_ = input().split(',')
# list_.sort()
# print(list_)

# list_ = [1, 2, 3]
# for i in list_:
#    if set(list_) == set(list_):
#       print('yes')
#       break
#    else:
#       print('ERROR')
#       break
# print(set(list_))
# print(list_[:])

# list_ = [1, 2, 3]
# list1 = [1, 2, 3]
# if set(list1) in set(list_):
#    print('aa')
# else:
#    print('a')

# list_ = list(range(54, 9184))
# for i in list_[:]:
#    if i % 5 == 0:
#       list_ = i
# print(list_)

# a1 = list(range(1, 100))
# print(a1[:])
# a = 'Kati'
# a.upper()
# # print(a)
# for i in '37808':
#     print(i)
#     continue
#     print(4)



# DICTIONARY

#Task1
# a = {'x' : 1, 'y' : 2, 'z' : 1}
# b = (list(a.keys())[list(a.values()).index(1)])
# print(b)

#Task2
# a = {'a': 1, 'b': 2, 'c': 1}
# deleted = a.pop('a')
# print(deleted)

#Task3
# a = {'a': 1, 'b': 2, 'c': 1}
# a.update({'f': 55})
# print(a)

#Task4
# a = {'a': 1, 'b': 2, 'c': 1}
# a.clear()
# print(a)

#Task5
# a = {'a': 1, 'b': 2, 'c': 1}
# keys = list(a.keys())
# print(keys)

#Task6
# a = {'a': 1, 'b': 2, 'c': 1}
# b = a.copy()
# print(b)

#Task7
# a = {'a': 1, 'b': 2, 'c': 1}
# for k in a:
#     print(k)

#Task8
# a = {'a': 1, 'b': 2, 'c': 1}
# for v in a.values():
#     print(v)

# a = list({'a': 1, 'b': 4, 'c': 1, 'd': 5, 'e': 6})
# b = dict()
# for v in a.values():
#     if v % 2 != 0:
#         continue
#     else:
#         b = dict(v)
# print(b)

# a = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25} 
# a['apple'] = 0.08
# a['orange'] = 0.06999999999999999
# a['banana'] = 0.05
# print(a)

# set1 = set(range(1, 20))
# print(set1)

# full_set = (set(set1) for set1 in range(1, 17))
# print(full_set)