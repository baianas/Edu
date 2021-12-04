# Строка - тип, хранящий текст
# Строка - неизменяемый, упорядоченный, индексируемый набор символов

# a1 = 'Строка'
# a2 = "Строка"
# a3 = '''Строка'''
# a4 = """Строка"""

# str1 = ''
# str2 = str()

# проверочные методы

# is...()

# isdigit() - проверяет, что все символы в строке являются цифрами

# a = 'string'
# b = '12344'

# a.isdigit() #False
# b.isdigit() #True

# isdecimal()
# isnumeric()

# isalpha() - проверяет, что все символы являются буквенными

# a = 'Test'
# b = 'Привет'
# c = 'Hello world'


# print(a.isalpha()) #True
# print(b.isalpha()) #True
# print(c.isalpha()) #False из-за пробела

# isalnum() - проверяет, что все символы либо буквы либо цифры

# a = 'test1'
# a1 = 'test2'
# a2 = 'test 3'

# a.isalnum()
# a1.isalnum()
# a2.isalnum()

# islower(), isupper()- проверяет, что все буквенные символы находятся в нижнем/верхнем регистре

# a1 = 'hello'
# a2 = 'Hello223'
# a3 = 'My string'
# a4 = 'TEST STRING'
# a5 = 'hello123'

# print(a1.islower()) #True
# print(a2.islower()) #False
# print(a3.islower()) #False
# print(a4.islower()) #False
# print(a5.islower()) #True

# a1.isupper() #False
# a2.isupper() #False
# a3.isupper() #False
# a4.isupper() #True
# a5.isupper() #False

# isspace() - проверяет, что все символы в строке являбтся пробельными

# ' ', '\n', '\t', '\r'

# методы, возвращающие преобразованную копию строки

# lower(), upper() - переводит все буквенные символы в нижний/верхний

# 'a' != 'A'

# a1 = 'My string'

# a1.lower() #'my string'
# a1.upper() #'MY STRING'

# capitalize() - преобразует первую букву в верхний регистр, а остальные в нижний

# a1 = 'привет'
# a2 = 'HELLO'
# a3 = '123, Downing str'
# a4 = '12345'
# a5 = 'сегодня плохая погода. пасмурно.'

# a1.capitalize() #'Привет'
# a2.capitalize() #'Hello'
# a3.capitalize() #'123, downing str'
# a4.capitalize() #'12345'
# a5.capitalize() #'Сегодня плохая погода. пасмурно'

# strinp(), rstrip(), lstrip() - убирает определенные символы по краям строки(по умол. пробельные символы)

# a = '    hello  \n'

# a.strip() #'hello'

# b = '***hello***'
# b.strip('*') #'hello'

# c = '---*****&&&&hello++++(((^^^'
# c.strip('-*&+(^') #'hello'

# d = '****hello****'
# print(d.strip('***')) #'hello'

# split() - разбивает строку по какому-то разделителю

# a = 'Tilek Ermek Janyl'
# a.split() #['Tilek', 'Ermek', 'Janyl']

# b = 'spam---eggs---milk'

# b.split(---) #['spam', 'eggs', 'milk']

# join() - объединяет список из строк в одну строку

# a = ['spam', 'eggs', 'milk']
# ','.join(a) #'spam, eggs, milk'

# replace() - заменяет один или несколько (группу) символов


# a = 'This is a test string'
# a.replace('a', '*') #Th*s *s a test str*ng'
# a.replace('i', '*', 2) #'Th*s s a test string'

# a.replace('test', 'default') #'This is a default string'

# b = 'String 1'
# b.replace(' ', '') #'String1'

#поиск в строке 

# in
# a = 'Good day'

# 'e' in a #False
# 'a' in a #True
# 'hello' in a #False
# 'day' in a #True
# 'good' in a #False из-за регистра

# find() - возвращает индекс первого вхождения подстроки

# strl = 'This is a test string'

# strl.find('s') #3
# strl.find('is') #2
# strl.find('o') #-1

# index() - возвращает индекс первого вхождения подстроки
# strl = 'This is a test string'

# strl.index('s') #3
# strl.index('is') #2
# strl.index('o') #ValueError
# strl.index('is', 4, 12) #5



# # count() = возвращает количество вхождений подстроки

# a = 'This is a test string'

# a.count('t') #3

# a.count('is') #2

# a.count('o') #0

# доступ к элементам

# a = 'My string'
#     #   012345678

# a[0] #'M'
# a[5] #'r'

# a[-1] #'g'
# a[-4] #'r'
# a[2] #' '

# #срез (slice)

# a = 'Test string'

# [старт:стоп:шаг]

# a[0:4:1] #'Test'
# a[:4] #'Test'
# a[:4:1] #'Test'
# a[5:8] #'str'

# a[-3:] #'ing'
# a[-3:len(a)] #'ing'
# a[-3:11] #'ing'

#длина строки

# a = 'string'
# len(a) #6

# b = 'my string'
# len(b) #9

# #конкатенация

# a = 'Hello'
# b = 'World'

# a + b #'HelloWorld'
# b + a #'WorldHello
# a + ' ' + b #'Hello World'


# #размножение строк

# a = '1'

# a * 5 #'11111'
# a.center(5, '1') #'11111'
# a.center(5, '*') #'**1**'

# #форматирование

# name = 'Андрей'
# time = '15:40'
# total = 25000

# check1 = 'Здравтвуйте, Иван! Ваш заказ принят в 18:05. Сумма заказа 15000'
# check2 = 'Здравтвуйте, Михаил! Ваш заказ принят в 18:05. Сумма заказа 15000'

# %

# name = 'Андрей'
# time = '15:40'
# total = 25000
# sample = 'Здравтвуйте, %s! Ваш заказ принят в %s. Сумма заказа %s.2f'

# res = sample % (name, time, total) 

# print(res)

# name = 'Андрей'
# time = '15:40'
# total = 25000

# sample = 'Здравтвуйте, {name}! Ваш заказ принят в {time}. Сумма заказа {total}.2f'


# res = sample.format(name, time, total)
# print(res)

# f - строки

# name = 'Андрей'
# time = '15:40'
# total = 25000

# res = f'Здравтвуйте, {name}! Ваш заказ принят в {time}. Сумма заказа {total}.'

# print(res)

# a = 10
# b = 20


# res = f'Произведение чисел a  и b равно {a * b}'

# print(res)





# a = '1'



# print(a.center(5, '*'))


# a = 'spameggs'

# a[1:4:1] #'pam

# print(a[7:4:-1]) #'sgg'