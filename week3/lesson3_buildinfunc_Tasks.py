#Task1
# list_ = [1, 2, 3, 4]
# result = sum(list_)

# print(result)

#Task2
# list_ = [1, 5, -9, 6, -4]
# result = all(int > 3 for int in list_)
# print(result)

#Task3
# list_ = [5, 8, 4, 6, 7]
# result = any(int < 0 for int in list_)
# print(result)

#Task4
# list_ = [1, 2, 3, 4]
# result = list(map(lambda x: x ** 2, list_))
# print(result)

#Task5
# list_ = [1, 2, 3, 4]
# result = list(filter(lambda x : x % 2 == 0, list_))
# print(result)

#Task6
# list_ = ['inheritance', 'solid', 'polymorphism', 'dry', 'yagni']
# result = list(filter(lambda word : len(word) > 7, list_))
# print(result)

#Task7
# import functools
# from functools import reduce
# list_ = [5, 6, 7, 8]
# result = reduce(lambda x, y : x * y, list_)
# print(result)

#Task8
# list_ = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even  = list(filter(lambda x : x % 2 == 0, list_))
# odd = list(filter(lambda x : x % 2 != 0, list_))
# result = f'even: {len(even)}, odd: {len(odd)}'
# print(result)

#Task9
# list_ = [-1, 2, 3, 5, -3, 7, ]
# result  = list(map(lambda x : x > 0, list_))
# print(result)

#Task10
# import functools
# from functools import reduce
# list_ = ['Paul', 'George', 'Ringo', 'John']
# result = reduce(lambda x, y : x if len(x) > len(y) else y, list_)
# print(result)


# import functools
# from functools import reduce

# string = 'Hello World'
# list_ = ['o', '*', '!']
# print(reduce(string.replace, list_))