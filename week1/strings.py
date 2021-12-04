# #Task1

# # data = input('Введите имя, фамилию и возраст через пробел:\n').split()
# # name = data[0]
# # last_name = data[1]
# # age = data[-1]

# # name = name.lower().replace('a', '').title()
# # last_name = '*'.join(list(last_name))
# # print((name + last_name) * int(age))


# #Task2

# data = input('Введите строку: ').lower()
# a = data.count('a')
# e = data.count('e')
# i = data.count('i')
# o = data.count('o')
# u = data.count('u')
# y = data.count('y')



# print(f'В вашей строке насчитано {a + e + i + o + u + y} гласных букв')


# #Task3

# username = input('Введите юзернейм: ')
# center = int(len(username)/2)


# new_username = username[:center] + '&' + username[center:] + '$'
# password = new_username.swapcase()
# print(f'Вам сгенерирован пароль: {password}')