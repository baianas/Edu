# num1 = int(input('Введите число: '))
# choice = input('Выберите действие(+,-,*,/,%,//): ')
# num2 = int(input('Введите второе число: '))

# if choice == '+':
#     result = f'{num1}{choice}{num2}={num1+num2}'
# elif choice == '-':
#     result = f'{num1}{choice}{num2}={num1-num2}'
# elif choice == '*':
#     result = f'{num1}{choice}{num2}={num1*num2}'
# elif choice == '/':
#     if num2 != 0:
#         print('Ответ:', num1 / num2)
#     else:
#         print('Деление на 0!')
#     result = f'{num1}{choice}{num2}={num1/num2}'
# elif choice == '%':
#     result = f'{num1}{choice}{num2}={num1%num2}'
# elif choice == '//':
#     result = f'{num1}{choice}{num2}={num1//num2}'
# else:
#     result = print('Данной операции нет в системе!')
# print(result)

# num1 = int(input('Введите число: '))
# choice = input('Выберите действие(+,-,*,/,%,//): ')
# num2 = int(input('Введите второе число: '))

# dict_ = {
#     '+': num1 + num2,
#     '-': num1 - num2,
#     '*': num1 * num2,
#     '/': num1 / num2,
#     '%': num1 % num2,
#     '//': num1 // num2
# }
# print(dict_[choice])


num1 = int(input('Введите первое число: '))
operation = input('Выберите операцию из следующих +-*/ : ')
num2 = int(input('Введите второе число: '))
print('Ответ: ')
if operation == '/' and num2 == 0:
    print('На 0 делить нельзя')
else:
    dict_ = {
    '+' : num1 + num2,
    "-" : num1 - num2,
    '*' : num1 * num2,
    '/' : num1 / num2
    }
    print(dict_.get(operation, ' Данной операции нет в системе'))
    # print(dict_[operation, ' Данной операции нет в системе'])


print(f'Ответ: {(eval(input("Введите действие: ")))}')

print(f'Ответ: {(eval(input("Введите действие: ")))}')

while True:print(eval(input('Введите действие: ')))