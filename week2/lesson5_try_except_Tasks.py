#Task2
# b = 10
# c = 11
# try:
#     print(a)
# except NameError:
#     print(('Такого значения нет'))


#Task3
# num1 = int(input())
# num2 = int(input())
# try:
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')


#Task4
# try:
#     num1 = int(input())
#     num2 = int(input())
#     res = num1 + num2
#     print(res)
# except ValueError:
#     print('Введите число!')


#Task5
# dict_ = {'key1': 'value1', 'key2': 'value2'}
# key = 'eege'
# try:
#     dict_[key]
# except KeyError:
#     print('Нет такого ключа!')
# else:
#     print(dict_[key])


#Task6
# list_ = [1, 4, 9, 16, 25, 36]
# try:
#     list_[11]
# except IndexError:
#     print('Нет такого элемента!')


# Task7
# try:
#     age = int(input())
#     if age < 18:
#         raise ValueError ('Доступ запрещён')
# except ValueError:
#     print('Введён некорректный возраст')
# else:
#     print('Спасибо')
# finally:
#     print('До свидания!')

#Task8
# try:
#     num1 = int(input())
#     num2 = int(input())
#     print(num1 / num2)
# except (ValueError, ZeroDivisionError):
#     print('Произошла ошибка!')

#Task9
# cash = int(input())
# if cash < 0:
#     raise ValueError ('Сумма не может быть отрицательной!')
# else:
#     print(cash)


#Extra Task 2

inp1 = input().split(' ')
list_ = []

for i in inp1:
    try:
        list_.append(int(i))
    except ValueError:
        raise Exception('Данный элемент не является числом!')

print(list_)