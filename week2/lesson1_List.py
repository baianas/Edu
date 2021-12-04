# # Список - изменяемый, упорядоченный набор произвольных элементов

# # a = []
# # b = list()

# # list1 = [1, 2, 3, 4]
# # list2 = ['Tim', 'Jack', 'John']
# # list3 = [1, 2, None, True]

# #В список можно добавлять элементы, удалять, и заменять

# # b = (1, 2, 3)

# # list1 = [1, 2, 3, 4, 5]
# #       #  0  1  2  3  4

# # list1 = ['Мясо', 'Картошка', 'Молоко']

# # queue = ['John', 'Tim', 'Ivan', 'Olga']

# # queue[0] #'John'
# # queue[1:3] #['Tim', 'Ivan']
# # queue[-1] #'Olga'
# # queue[4] #IndexError

# #добавление элементов
# # a = [1, 2, 3, 4, 5]

# # #append(element) - добавляет элемент в конце списка

# # a = [1, 2, 3, 4, 5]
# # a.append(6)
# # a #[1, 2, 3, 4, 5, 6]
# # # a.insert(5, 6)

# # #insert(index< element) - вставляет элемент на указанный индекс

# # a = [1, 2, 3, 4, 5]
# # a.insert(0, 0)
# # a  #[0, 1, 2, 3, 4, 5]

# # # extend(list) - добавляет элементы другого списка в конец текущего

# # a = ['Tim', 'Jenny', 'Tanya']
# # b = ['John', 'Max']
# # a.extend(b)
# # a #['Tim', 'Jenny', 'Tanya', 'John', 'Max']

# #конкатенация 
# a = [1, 2, 3]
# b = [4, 5, 6]

# print(a + b) #[1, 2, 3, 4, 5, 6]
# print(a) #[1, 2, 3]
# print(b) #[4, 5, 6]

# # #замена элементов

# # a = [1, 2, 3]

# # a[2] = 10

# # a #[1, 2, 10]

# # a = [[1, 2, 3], 4]
# # a[0] #[1, 2, 3]
# # a[0].append(4)
# # a #[[1,2,3,4], 4]

# #удаление элементов

# # pop() - удаление по индексу
# # list1 = [1, 2, 3, 4, 5]
# # list1.pop()
# # print(list1)

# # list1 = [1, 2, 3, 4, 5]
# # list1.pop(3)
# # print(list1)

# # list1 = [1, 2, 3, 4]
# # list1.pop(5)  #IndexError

# # list1 = [1, 2, 3, 4, 5]
# # last = list1.pop()

# # remove(value) - удаляет по значению
# # a = ['a', 'b', 'c', 'd']
# # a.remove('b')
# # print(a)

# # list1 = [1, 2, 3, 1, 1, 2, 3]
# # list1.remove(1)
# # print(list1) #[2, 3, 1, 1, 2, 3]

# # # clear()- очищает список(удаляет все элементы)

# # my_list = [1, 2, 3, 4]
# # my_list.clear()
# # my_list #[]

# # # del()

# # a = ['a', 'b', 'c', 'd']
# # a[-1]
# # del a[3]
# # a #['a', 'b', 'c']

# # del a 

# #index(value) - возвращает индекс первого элемента с указанным значением

# # a = [1, 2, 3, 2, 4, 2]
# # a.index(2) #1

# # #count(value) - возвращает число, сколько раз встречается элемент с указанным значением
# # a = [1, 2, 3, 2, 4, 2]
# # a.count(2) #3

# # a = [1, 2, 3, 4]
# # lena(a) #4
# # a1 = ['12345', [12, 3, 4], (1,2,3)]
# # len(a1) #3

# #in - проверка на вохждение

# # list1 = [12, 234, 11, 23]

# # value1 = 11
# # value2 = 13

# # value1 in list1 #True
# # value2 in list1 #False

# #sort() - сортирует список

# # a = [12, 1, 23, 4, 21, 2, 34]
# # # a.sort()
# # # a #[1, 2, 4, 12, 21, 23, 34]

# # a.sort(reverse=True)
# # a #[34, 23, 21, 12, 4, 2, 1]

# #reverse() - переворачивает список

# # a = [12, 22, 11, 23, 34, 42, 1]

# # a.reverse()
# # # a[::-1]

# # a #[1, 42, 34, 23, 11, 22, 12]

# # #размножение списка

# # a = [0]
# # a * 5 #[0, 0, 0, 0, 0]

# #копирование списка

# # a = [1, 2, 3]

# # b = a.copy()
# # # b = a[:]
# # # from copy import copy
# # # b = copy(a)

# # a[0] = 10
# # print(b)

# # a = [1, 2, 3, 4, 5]
# # b = range(1,6)
# # #[1, 2, 3, 4, 5]

# # list(b)
# # b[0]
# # for num in b


# # a = range(6).__iter__()

# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))
# # print(next(a))

# # a = [1, 2, 3, 4, 5]
# # цикл - это многократное выполнение определенного действия / действий
# # while, for
# # while - многократное проверка условия(цикл выполняется до тех пор выполняется условие)

# # for - цикл для обхода последовательностей(iterable): строка, списки, кортежи, словарь, множества, range().
# # Цикл выполняется до тех пор, пока последовательности не исчерпаются элементы

# # Дана последовательность, необходимо обойти все элементы и распечатать каждый

# # list1 = [1, 2, 3, 4, 5]

# # for number in list1:
# #     print(number)

# # for i in list1:
# #     print(i)

# # for item in list1:
# #     print(item)

# list1 = [1, 2, 3, 4, 5]
# for item in list1:
#     print(item ** 2)

# list1 = ['tim', 'john', 'jack']
# for name in list1:
#     print(name.capitalize())


# list1 = ['tim', 'john', 'jack']
# new_names = []
# for name in list1:
#     new_names.append(name.capitalize())

# str1 = 'My string'
# list(str1) #['M', 'y', ' ', ....]

# a = '123456'
# for char in a:
#     print(char)

# a = [12, 23, 34, 45, 56, 67, 78, 89, 90, 41]

# в новый список собрать числа, которые кратны 3
# res = [12, 45, 78, 90]
# res = []
# for num in a:
#     if num % 3 == 0:
#         res.append(num)

# print(res)


# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# for i in a:
#     for j in i:
#         print(j)

# break - принудительная остановка цикла
# continue - пропуск итерации
# итерация - один проход цикла

# list1 = [1, 42, 21, 32, 34, 0, 5, 56]

# #распечатать сумму всех чисел, которые идут до 0

# total_ = 0
# for i in list1:
#     if i == 1:
#         break
#     else:
#         total_ += i

# print(total_)

# a = [12, 31, 42, 345, 23, 21, 34, 74, 22, 45, 78, 91]

# #пройтись по списку и посчитать сумму всех чисел, которые кратны 3

# total = 0
# for num in a:
#     if num % 3 == 0:
#         total += num


# total = 0
# for num in a:
#     if num % 3 != 0:
#         continue
#     total += num

# names = ['Alina', 'Timur', 'Aidai', 'Maksat', 'Alibek']
# #вывести имнена, которые не начинаются 'А'

# for name in names:
#     if not name.startswith('A'):
#         print(name)

# for name in names:
#     if name.startswith('A'):
#         continue
#     print(name)