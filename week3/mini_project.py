import random

name = input('What is your name?: ')
answer = input('Do you want to play? (Y/N): ')
secret = random.randint(1,15)
print(secret)

attempt = 0
while True:
    attempt += 1
    if attempt > 6:
        print(f'Sorry, {name}. You have lost')
        secret = random.randint(1,15)
        answer = input('Do you want to try one more time? (Y/N): ')
        print(secret)
        attempt = 0
        continue
    if answer.lower().strip() == 'y':
        try:
            guess = int(input(f'Guess the number.\n\
You have 5 lifes. This is your {attempt} attempt: '))
        except ValueError:
            print('Sorry, please enter the number')
            continue
    if guess == secret:
        print(f'Congratluations, {name}.')
        secret = random.randint(1,15)
        asnwer = input('Do you want to test your luck one more time? (Y/N): ')
        print(secret)
        # attempt = 0
    elif answer.lower().strip() == 'n':
        print(f'Ok. Goodbye, {name}')
    else:
        print('I do not understand')
