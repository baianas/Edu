# def get_formted_name(name:str, middle_name = None, last_name = 'Wick'):
#     """Выводит имя и фамилию"""
#     if middle_name:
#         return name + " " + middle_name + ' ' + last_name
#     return name + " " + last_name

# print(get_formted_name('John', middle_name='Anthony'))

# m = list(map(int, ['1', '2', '3', '4']))
# print(m)

# f = tuple(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# print(f)

# d = dict(zip([1, 2, 3], ['a', 'b', 'c']))
# print(d)


#Tasks
# def sum_range(start, end):
#     if start > end:
#         start, end = end, start
#     sum1 = sum(range(start, end +1))
#     return sum1

# print(sum_range(10, 1))


# def season(months):
#     if months < 1 or months > 12:
#         raise ValueError('Ошибка')
#     elif months in range(3, 6):
#         print('Весна')
#     elif months in range(6, 9):
#         print('Лето')
#     elif months in range(9, 12):
#         print('Осень')
#     else:
#         print('Зима')

# season(1)


def date(day, month, year):
    if day < 1 or day > 31:
        raise ValueError('Wrong day')
    
    if month < 1 or month > 12:
        raise ValueError('Wrong month')

    if year < 0 or year > 2022:
        raise ValueError('Wrong year')

    return True

print(date(3, 12, 2021))