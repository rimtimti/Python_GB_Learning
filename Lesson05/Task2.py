import defs
import random
import os
os.system('cls')

def get_positive_number_less_x_or_y(input_string: str, num1: int, num2: int)-> int:
    '''
    Просит у пользователя ввести целое число и проверяет, чтобы оно было меньше первого и второго числа
    '''
    try:
        number_int = int(input(input_string))
        if number_int <= 0:
            print('Вы ввели отрицательное число или ноль!!!')
            return get_positive_number_less_x_or_y(input_string, num1, num2)
        elif number_int > num1 or number_int > num2:
            print('Число больше, чем необходимо!!!')
            return get_positive_number_less_x_or_y(input_string, num1, num2)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_positive_number_less_x_or_y(input_string, num1, num2)

def check_positive_number_less_x_or_y(number: int, num1: int, num2: int)-> int:
    '''
    Проверяет, чтобы начальное число было меньше первого и второго числа
    '''
    if number > num1 or number > num2:
        return check_positive_number_less_x_or_y(number, num1, num2)
    else:
        return number

print('Перед вами игра: на столе лежит заданное в начале игры число конфет. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.\nЗа один ход можно забрать не более чем также заданное вами в начале игры число конфет. Тот, кто берет последнюю конфету - проиграл.')
number_of_sweets = defs.get_number_natural_int('Введите начальное число конфет на столе: ')
take_sweets_in_one_move = get_positive_number_less_x_or_y('Введите число конфет, которое можно брать за один ход: ', number_of_sweets, number_of_sweets)
players = ['player1']
a = get_positive_number_less_x_or_y('Выберите с кем будете играть (с другим человеком - 1, с глупым ботом - 2, с умным ботом - 3): ', 3, 3)
if a == 1:
    players.append('player2')
if a == 2:
    players.append('bot')
else:
    players.append('clever_bot')

i = random.randint(0, 1)
print(f'Первый ход достается игроку {players [i]}')
while number_of_sweets > 1:
    if a == 1 or i == 0:
        move = get_positive_number_less_x_or_y(f'Игрок {players [i]}, сколько конфет вы забираете?: ', take_sweets_in_one_move, number_of_sweets)
    elif a == 2:
        move = check_positive_number_less_x_or_y(random.randint(1, take_sweets_in_one_move), take_sweets_in_one_move, number_of_sweets)
        print(f'Игрок {players [i]} забирает {move} конфет.')
    else:
        if number_of_sweets % (take_sweets_in_one_move + 1) == 1:
            move = check_positive_number_less_x_or_y(random.randint(1, take_sweets_in_one_move), take_sweets_in_one_move, number_of_sweets)
        else:
            move = (number_of_sweets - 1) % (take_sweets_in_one_move + 1)
        print(f'Игрок {players [i]} забирает {move} конфет.')
    number_of_sweets -= move
    i = (i+1)%2
    print(f'Ход достается игроку {players [i]}, осталось {number_of_sweets} конфет.')
else:
    print(f'Игрок {players [i]} проиграл.... печалька (')