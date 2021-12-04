# def func(a, b):
#   res = a + b
#   return res

# print(func(5, 6))

# def func1(a, b):
#   print(type(a))
#   print(type(b))

# func1(6, 'asad')

# def func2(*nums):
#   return sum(nums)

# print(func2(5, 6, 7, 9))

# def func3(string: str):
#     glas = 0
#     soglas = 0
#     symbols = 0
#     for i in string:
#         if i.lower() in 'йуеыаоэяию':
#             glas += 1
#         elif i.isalpha():
#             soglas += 1
#         else:
#             symbols += 1
#     return(f'Гласные: {glas}, согласные: {soglas}, символы:{symbols}')
        
    
# print(func3('Мурат супер!'))

# a = [5, 6, 3, 2 ,7, 4]
# b = all(x > 3 for x in a)
# print(b)
# all

# list_ = [-1, 2, 3, 5, -3, 7, ]
# result  = list(map(lambda x : x > 0, list_))
# print(result)

# all

# import functools
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x, y : x if len(x) > len(y) else y, list_)
# print(result)

# def func3(string: str):
#   glas = 0
#   soglas = 0
#   symbols = 0
#   for i in string:
#     if i.lower() in 'йуеыаоэяию':
#       glas += 1
#     elif string.isalpha():
#       soglas += 1
#     else:
#       symbols += 1
    
# print(func3('Мурат супер!'))

Max = input('Введите имя: ')
if Max == 'Макс':
    print(f'{Max} конченный гандон')
else:
    print(f'{Max} красавчик')