
user_number1 = float(input('Введите цифру : '))
user_number2 = float(input('Введите цифру : '))
user_action = input('Выберите действие +, -, /, *, mod, pow, div ')

if user_action == '+':
    print(user_number1 + user_number2)
elif user_action == '-':
    print(user_number1 - user_number2)
elif user_action == '/':
    print(user_number1 / user_number2)
elif user_action == '*':
    print(user_number1 * user_number2)
elif user_action == 'mod':
    print(user_number1 % user_number2)
elif user_action == 'pow':
    print(user_number1 ** user_number2)
elif user_action == 'div':
    print(user_number1 // user_number2)
