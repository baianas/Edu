# def add(a, b):
#     return a+b
    
# res = add(b = 1,a = 3)
# print(res)


# def list(*elements, **kwargs):
#     if 'step' in kwargs:
#         step = kwargs.get('step')
#         res = []
#         for index, element in enumerate(elements):
#             if index == 0:
#                 res.append
#             elif step % index:
#                 res.append(element)
#         return res
#     else:
#         return[*elements]

# print(list(1, 2, 3, step = 2))




# def hello(age, name='Guest'):
#     print(f'Hello, {name}! Your age is {age}')

# hello(12, 'Admin')

# def add_func(num1, num2):
#     return num1 + num2

# def sub_func(num1, num2):
#     return num1 - num2

# def mult_func(num1, num2):
#     return num1 * num2

# def div_func(num1, num2):
#     return num1 / num2

# def handler(operator, num1, num2):
#     dict_ = {"+":add_func,
#                 "-":sub_func,
#                 "*":mult_func,
#                 "/":div_func}
#     if not dict_.get(operator):
#         return "Введен некоректный оператор"
#     if operator == '/' and num2 == 0:
#         return "На 0 делить нельзя"
#     return dict_.get(operator)(num1, num2)

# num1 = int(input('Num1'))
# operator = input()
# num2 = int(input('num2'))

# print(handler(operator, num1, num2))

def translate(string):
    intab = "qwertyuiop[]asdfghjkl;'zxcvbnm,."
    outtab = "йцукенгшщзхъфывапролджэячсмитьбю"
    if string[0] in intab:
        trantab = str.maketrans(intab, outtab)
    else:
        trantab = str.maketrans(outtab, intab)
    return string.translate(trantab)

string = input('Vvedite stroku: ')
print(translate(string))