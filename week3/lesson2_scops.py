# a = "Это глобальная переменная"
# print(id(a))
# def func():
#     # global a
#     a = "Это enclosed переменная"
#     print(id(a))
#     print(a)
#     def inner_func():
#         nonlocal a
#         a = "Это локальная переменная"
#         print(id(a))
#         print(a)
#     inner_func()

# func()
# print(a)

# num1 = 5
# num2 = 4

# def sum(a, b):
#     global num1
#     num1 = a + b
#     return a + b

# print(sum(num1, num2))
# print(sum(num1, num2))
# print(sum(num1, num2))
# print(sum(num1, num2))

# def outter_func():
#     print('outter')

#     def inner_func():
#         print('inner')

#     return inner_func

# inner_func = outter_func()

# outter_func()()

# a = 5
# b = 3

# print(globals())
# print(locals())

# def func():
#     c = 2
#     print(locals())

# func()





# x = 0

# def counter():
#     global x
#     print(x)
#     x += 1

# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# counter()
# print(x)


def func1(a):
    a = a + 10
    def func2():
        nonlocal a
        a = a + 100
        def func3():
            nonlocal a
            a = a + 1000
        func3()
    func2()

    return func2()

print(func1(5))
# func1(5) -> 115