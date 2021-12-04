#admin@gmail.com
#username = admin
# url = gmail.com


def check_valid(email):
    try:
        username, url = email.split('@')
        website, extension = url.split('.')
    except ValueError:
        print('Please, enter your email correctly')
        return False

    if not username.replace('-', '').replace('_', '').isalnum():
        print('Email cannot contain free spaces')
        return False
    if not website.isalnum():
        return False
    if len(extension) > 3:
        print('extension cannot be more than 3 symbols')
        return False
    return True

n = input('How many emails do you want to registrate?  ')

if n.isalpha():
    raise ValueError('Please enter the number correctly!')
else:
    emails = [input('Please, enter your emails: ') for email in range(int(n))]


valid = list(filter(check_valid, emails))

print(f'Validated emails: {sorted(valid)}')
