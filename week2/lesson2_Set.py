# кортеж - неизменяемый упорядоченный набор произвольных элементов

#кортеж не позволяет добавлять, заменять и удалять элементы

# a = ()
# b = tuple()
# c = 1,2,3 #(1,2,3)

# x = 10
# y = 20

# x, y = y, x 
# x, y = (20, 10)
# # x, y = [20, 10]

# index(value) - возвращает индекс первого элемента с указанным значением

# count(value) - считатет количество элементов с указанным значением

# a = (1,2,3,4)
# a[0] #1
# a[-1] #4
# a[1:3] #(2,3)

# #конкатенация

# a = (1,2,3)
# b = (4,5,6)

# a + b #(1,2,3,4,5,6)

# a = (1,2,3)
# b = a
# print(id(a))
# print(id(b))

# a = (1,2,3,4)
# len(a)

# a = (1,2,3,4)
# value1 = 10
# value2 = 3

# value1 in a #False
# value2 in a #True

#итерация по кортежам

# a1 = [1,2,3,4,5]
# a2 = (1,2,3,4,5)

# for i in a1:
#     print(i)

# for i in a2:
#     print(i)

# a = (1, 2, 3, 4, 5)
# b = list(a)

# a = [1, 2, 3, 4, 5]
# b = tuple(a)

#множества 
# множество - неупорядоченный изменяемый набор уникальных неизменяемых элементов

# изменяемые типы:
# - списки
# - словари
# - множества

# неизменяемые типы:
# - числа(целые, дробные)
# - строки
# - кортежи
# - frozenset()
# - boolean
# - None

# a = set()

# b = {1, 2, 3}

# a = {[1, 2, 3], {1,2,3}} #ошибка

# b = {1, 2, 3, 4, 1, 2, 3}

# print(b) #{1, 2, 3, 4}

# добавление элементов
# add(element) - добавляет элемент во множество

# a = {'a', 'b', 'c'}
# a.add('0')
# print(a) #{'b', '0', 'a', 'c'}

# update(set) - добавляет элементы множества в текущее множество

# a1 = {1, 2, 3, 4}
# b1 = {4, 5, 6, 7}

# a1.update(b1)
# print(a1)
# print(b1)


# # удаление элементов
# discard(element) - удаляют указанный элемент. Если элемента нет, то ничего не происходит
# remove(element) - удаляют указанный элемент. Выдаёт KeyError, если элемента нет
# pop() - удаляет произвольный элемент
# clear() - очищает множество

#пересечение - общие элементы

# physics = {'Tim', 'Jack', 'Anna'}

# chemistry = {'Jack', 'Inna', 'Olga'}

# math = {'Hailey', 'George', 'Jack'}

# physics.intersection(chemistry, math) #{'Jack'}

# physics & chemistry & math #{'Jack'}

# #объединение - все элементы из нескольких множеств за исключением дубликатов


# physics = {'Tim', 'Jack', 'Anna'}

# chemistry = {'Jack', 'Inna', 'Olga'}

# math = {'Hailey', 'George', 'Jack'}

# physics.union(chemistry, math) #{'Tim', 'Jack', 'Anna', 'Inna', 'Olga', 'Hailey', 'George'}


# physics | chemistry | math #{'Tim', 'Jack', 'Anna', 'Inna', 'Olga', 'Hailey', 'George'}

#разность


# physics = {'Tim', 'Jack', 'Anna'}

# chemistry = {'Jack', 'Inna', 'Olga'}

# math = {'Hailey', 'George', 'Jack'}

# physics.difference(chemistry) #{'Tim', 'Anna'}

# physics - chemistry #{'Tim', 'Anna'}

# #симметричная разность - объединение разных элементов двух или более элементов

# physics = {'Tim', 'Jack', 'Anna'}

# chemistry = {'Jack', 'Inna', 'Olga'}

# physics - chemistry #{'Tim', 'Jack'}
# chemistry - physics #{'Inna', 'Olga'}

# physics.symmetric_difference(chemistry) #{'Tim', 'Anna', 'Inna', 'Olga'}
 
# physics ^ chemistry
# chemistry ^ physics

# (physics - chemistry) | (chemistry - physics)

# (physics | chemistry) - (physics & chemistry)

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # a & b -> {4, 5}
# a.intersection_update(b)
# a = a & b
# a & b = b


#update
# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # a.update(b)
# a #{1, 2, 3, 4, 5, 6, 7, 8}

# a = a | b

# #difference_update() - находит разность и ей заменяет множество

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# # a - b {1, 2, 3}

# a = a -b
# a -=b




# # symmetric_difference_update()

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}

# a ^ b #{1, 2, 3, 4, 5, 6, 7, 8}

# a.symmetric_difference_update
# a #{1, 2, 3, 4, 5}

# a = a ^ b

# #подмножество - часть какого-либо множества

# class1 = {'Tim', 'John', 'Inna', 'Anna', 'Maria', 'Ivan'} #надмножество roup

# group = {'Ivan', 'Maria'} #подмножество

# group2 = {'Nik', 'Max', 'Inna'} #не является подмножеством от class1

# group.issubset(class1) #True
# group2.issubset(class1) #False

# class1.issuperset(group) #True
# class1.issuperset(group2) #False

# isdisjoint() - проверяет, пересекаются ли 2 множества

# a = {1, 2, 3, 4, 5}
# b = {4, 5, 6, 7, 8}
# c = {6, 7, 8, 9, 10}

# a.isdisjoint(b) #False
# a.isdisjoint(c) #True

# a1 = {1, 2, 3}
# b1 = {1, 2, 3}
# c1 = {1, 2, 6}

# a1 == b1 #True
# a1 == c1 #False

# list1 = [1, 2, 3, 4, 5, 1, 2, 3]
# res = list(set(list1))

# res #[1, 2, 3, 4, 5]

# counter = 0

# while counter < 10:
#     print('Hello World')
#     counter += 1

# a = 10
# b = 10
# a = a + 2 #12
# print(a)
# print(b)

# a = 'string'
# a = a.upper() #'STRING'
# print(a)