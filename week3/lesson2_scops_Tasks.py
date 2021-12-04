#Task1
# def foo():
#     global var
#     var = 'переменная foo'
#     def bar():
#         global var
#         print(f"переменная в foo:  {var}")
#         var = 'переменная bar'
#     bar()
# foo()
# print("переменная в foo: ", var)


#Task2
# x = 'Я глобальная переменная!'
# def my_func():
#     global x
#     print('Я глобальная переменная!')
#     x = 'Я могу изменяться'

# my_func()
# print(x)
# print(globals())


#Task3
# num = 3
# def mul():
#     global num
#     num **= 2
#     return num

# mul()
# mul()
# mul()
# print(num)


#Task4
# balance = 0
# def get_salary(amount):
#     global balance
#     balance += amount
    
# def pay_bills(amount, log_name):
#     global balance
#     balance -= amount
#     print(f'Вы заплатили {amount} сом за {log_name}')

# def get_balance():
#     print(f'У вас на счету {balance} сом')
    
# get_salary(1000)
# get_balance()
# pay_bills(400, 'кабельное тв')
# get_balance()


#Task5
# result = 0
# def pow_first(x,y):
#     global result
#     result = x**y

# def pow_second(z):
#     global result
#     result %= z
#     return result
    
# pow_first(2, 3)
# pow_second(3)
# print(result)


#Task6
# a = {'Мурат': 24, 'Эржан': 21, 'Чынгыз': 24, 'Алтынай': 17, 'Асема': 16}

# def age_control():
#     for i in a:
#         if a[i] >= 17:
#             print(f'{i}, Вы можете войти в клуб')
#         else:
#             print(f'{i}, извините, Вы не проходите по age-control')

# age_control(a)

#Task7.1
# a = ['pipi', 'papa', 'mama']

# def title_():
#     b = [i.title() for i in a]
#     return b

# b = title_(a)    
# print(title_())

#Task7.2
# a = ['pipi', 'papa', 'mama']
# b = []
# def title_():
#     global a
#     for i in a:
#         b.append(i.title())
#     print(b)
        
# title_()


#Task8
# def count_symbols(word):
#     vowels = 0
#     consonants = 0
#     symbols_ = 0
#     symbols = '`~!@#$%^&*()_+-=[] ;:"|\,.<>?/'
#     for letter in word:
#         if letter.isalpha():
#             if letter.lower() in 'ауоыиэяюёе':
#                 vowels += 1
#             else:
#                 consonants += 1
#         if letter in symbols:
#             symbols_ += 1
        
 
#     return (f'Количество гласных: {vowels}, согласных: {consonants}, остальных символов:{symbols_}')

# print(count_symbols('Мурат супер!'))

# def count_symbols(string: str):
#     soglas = 0
#     glas = 0
#     symbols = 0
#     for i in string.lower():
#         print(i)
#         if i in 'ауоыиэяюёе':
#             glas += 1
#         elif i.isalpha():
#             soglas +=1
#         else:
#             symbols += 1

#         return (f'Количество гласных: {glas}, согласных: {soglas}, остальных символов:{symbols}')

# print(count_symbols('Мурат супер!'))
#Task9
# a = []

# def num():
#     global a
#     for x in range(0, 11):
#         a.append(x)
#     return a

# print(num())


#Task10
# a = [1, 3, 4, 6, 8, 6, 8, 9, 0, 3]

# def nums():
#     for x in a:
#         if x < 7:
#             print(x)

# nums()