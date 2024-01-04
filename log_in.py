expected_user = 'Jason'
expected_pwd = 'BadDog1234'
expected_email = 'jason@gmail.com'
actual_user, actual_pwd, actual_email = input('enter the user name: '), input('enter password: '), input('enter email: ')
number_of_if = 0
number_of_else = 0
if actual_user.lower() == expected_user.lower():
    print(f'User name correct')
    number_of_if += 1
    if actual_pwd == expected_pwd:
        print(f'correct password')
        number_of_if += 1
        if len(expected_pwd) > 7:
            print(f'The password must contain letter and also numbers')
        if actual_email.lower() == expected_email.lower():
            print(f'Log in successful')
            number_of_if += 1
        else:
            print('wrong email. Please try again')
            number_of_else += 1
            new_email = input(f'enter email again')
            if new_email == expected_email:
                print(f'looking good')
                number_of_if += 1
            else:
                print(f"Wrong email. You`re account is blocked")
                number_of_else += 1
    else:
        print(f'Wrong password')
        number_of_else += 1
else:
    print(f'Wrong user. Please try again')
    number_of_else += 1
print(f'You used IF for {number_of_if} times')

number_of_else += 1
print(f'You used Else for {number_of_else} times')

geometric_shape = 'triangle'
step = '*'
print(geometric_shape[0:4])
print(geometric_shape[0] + step + (geometric_shape[2] + step) + (geometric_shape[4] + step) + (
        geometric_shape[6] + step))
