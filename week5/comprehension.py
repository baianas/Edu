# n = [x for x in range(70, 100) if x % 2 == 0]
# print(n)

# str_list = ['4', '6']
# x = [int(y) for y in str_list]
# print(x)

# names = ['Valentin', 'Petr', 'Anna', 'Evgeniy', 'Konstantin', 'Valeria', 'Yulia']

# x = [y for y in names if len(y) <= 5]
# print(x)

# nums = [2, 77, 12, 3, 0, 112, 4, -987]
# num = [n * 2 if n <5 else n -2 for n in nums]
# print(num)

# x = int(input('enter number: '))
# nums = [print(i**2) for i in range(0, x)]
# # print(nums)



"""6. Создайте список list_ из чисел от 1 до 10 (включительно), заменяя четные числа - строкой 'четное', 
нечетные добавьте без изменений."""

# list_ = ['четное' if x % 2 == 0 else x for x in range(1, 11)]
# print(list_)



"""7. Дан словарь где ключами являются фрукты, а значением их цены. При помощи dict comprehension создайте новый словарь где будут только те элементы, значение которых будет чётным."""

# fruits = {'apple': 25, 'banana': 40, 'mango': 17, 'orange': 12}

# dict_ = {k: v for k,v in fruits.items() if v % 2 == 0}
# print(dict_)


"8. Дан словарь 'a' в котором значениями являются целые числа. Пройдитесь по элементам и запишите в dict_ значения в виде списка чисел от 1 до числа, которое является значением."

a = {'a': 1, 'b': 5, 'c': 4, 'd': 3}

dict_ = {k: list(range(1, v+1)) for k, v in a.items()}
print(dict_)