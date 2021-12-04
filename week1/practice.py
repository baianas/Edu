#Task1

# password = input()
# if password.isdigit() and len(password) >= 8:
#     print('Ваш пароль сохранен')
# elif password.isdigit() and  len(password) < 8:
#     print('Ваш пароль должен содержать не менее 8 символов')
# elif not password.isdigit() and len(password) >= 8:
#     print('Ваш пароль должен хранить только числа')
# else:
#     print('Ваш пароль должен содержать не менее 8 символов\nВаш пароль должен содержать только буквы')


#Task2

# balls = input('Введите свои баллы по математике, английскому языку и литературе через запятую: ').split(', ')
# math = int(balls[0])
# english = int(balls[1])
# litr = int(balls[-1])
# average = (math + english + litr) / 3
# if average > 69:
#     print(f'Вы допущены к экзаменам. Ваш средний балл составляет {round(average, 1)}')
# else:
#     print('Вы не допущены к экзаменам')

# Task3

# import random
# play = ['Камень', 'Ножницы', 'Бумага']
# users_choice = input('Ваш выбор: ').capitalize()
# computer_choice = random.choice(play)

# if users_choice == 'Ножницы' and computer_choice == 'Бумага':
#     print(f'Выбор компьютера: {computer_choice}\nВы выиграли')
# elif users_choice == 'Ножницы' and computer_choice == 'Камень':
#     print(f'Выбор компьютера: {computer_choice}\nВы проиграли')
# elif users_choice == 'Бумага' and computer_choice == 'Камень':
#     print(f'Выбор компьютера: {computer_choice}\nВы выиграли')
# elif users_choice == 'Бумага' and computer_choice == 'Ножницы':
#     print(f'Выбор компьютера: {computer_choice}\nВы проиграли')
# elif users_choice == 'Камень' and computer_choice == 'Ножницы':
#     print(f'Выбор компьютера: {computer_choice}\nВы выиграли')
# elif users_choice == 'Камень' and computer_choice == 'Камень':
#     print(f'Выбор компьютера: {computer_choice}\nВы проиграли')
# elif (users_choice == 'Ножницы' and computer_choice == 'Ножницы') or \
#     (users_choice == 'Бумага' and computer_choice == 'Бумага') or \
#         (users_choice == 'Бумага' and computer_choice == 'Бумага'):
#     print(f'Выбор компьютера: {computer_choice}\nНичья')
# else:
#     print()