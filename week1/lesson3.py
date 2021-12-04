#условные операторы

#операции сравнения
# ">", "<", "==", "!=,<>", ">=", "<="

# '1' < 'A'
# 'A' < 'a'
# 'a' < 'b'

# 'abc' < 'abd'
# 'abc' < 'abcd'

# print(ord('c')) #99

# in #проверка на вхождение
# is #проверка на идентичность

#методы типов
# isupper(), islower(), startstwith()

# isinstance() - функция, проверяет относится ли объект копределенному классу

# a = 5

# isinstance(a, int) #True
# isinstance(a, str) #False

# issubclass(class1, class2) - проверяет, является ли class1 потомком class2

# class A:
#     pass

# class B(A):
#     pass

# class C:
#     pass

# issubclass(B, A) #True
# issubclass(C, A) #False

#False
# bool(0)
# bool('')
# bool(None)
# bool([])
# bool(())
# bool({})
# bool(set())
# bool(frozenset())

# #True
# bool(-1)
# bool(10)
# bool(1.4)
# bool(' ')
# bool('123')
# bool[1, 2, 3]
# bool((1, 2, 3))
# bool({'a': 1, 'b' : 2})
# bool{1, 2, 3}

# if условие:
#     действие

# num = 10
# if num > 5:
#     print('Ok!')



# a = [1, 2, 3, 4]

# value = 3

# if value in a:
#     print('Состоит в списке')


# str1 = 'Heelo world'

# if str1[0] == 'H'
# if str1.startswith('H'):
#     print('Ok!')

# a = (1, 2, 3)

# if len(a) > 0:
#     print('Ok!')


# if bool(a):
#     print('...')

# if a:
#     print('...')


# a = None

# if a is not None:
#     print('...')

# if a:
#     print('...')

# заглушка
# if a:
#     pass / #либо "..."

# True/False -> 1/0

# num = 10

# if num % 5 == 0:
#     print('...')
# else:
#     print('Bad!')

# число от 0 до 200

# от 0 до 40 - слабо
# от 40 до 80 - средне
# от 80 до 120 - нормально
# от 120 до 160 - сильно
# от 160 до 200 - опасно

# num = 158

# if num > 0 and num < 40:
#     value = ('слабо')
# elif num >= 40 and num < 80:
#     value = ('средне')
# elif num >= 80 and num < 120:
#     value = 'нормально'
# elif num >= 120 and num < 160:
#     value = 'silno'
# else:
#     value = 'opasno'

# and, or, not - логические операторы

# and - 'И'
# or - 'Или'
# not - 'НЕ'

# #end

# False and False -> False
# False and True -> False
# True and False -> False
# True and True -> True

# # or

# False or False -> False
# False or True -> True
# True or False -> True
# True or True -> True

# #not
# not True -> False
# not False -> True

#match case (switch case)
#3.10

# num = 10

# if num < 10:
#     ...

# if num == 10:
#     ...


# num = 100

# match num:
#     case 10:
#         ...
#     case 20:
#         ...
#     case 30:
#         ...
#     case _:
#         ...

# if num == 10:
#     ...
# elif num == 20:
#     ...
# elif num == 30:
#     ...
# else:
#     ...


# a = None

# if a != None:
#     ...

# if a is/is not None

# a = 10
# b = 20

# if (a > 10 and b < 30) or a % 5 == 0:

# a = [1, 2, 3, 4, 5]

# value = 5

# if value not in a:
#     print('Ok!')

# if not value in a:
#     print('Ok!')

# [1, 2, 3, 4, 5]

# range(1, 6)