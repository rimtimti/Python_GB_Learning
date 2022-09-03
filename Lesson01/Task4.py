def GetNumberInt():
    while type:
        number_int = input()
        try:
            number_int = int(number_int)
        except ValueError:
            print('Неверный ввод числа!!!')
        else:
            break
    return number_int


def GetRangeValue(number):
    if number < 1 or number > 4:
        print('Такой координатной четверти не существует !')
    elif number == 1:
        print('Возможные значения координат в I четверти: X (0, + ∞) , Y (0, + ∞)')
    elif number == 2:
        print('Возможные значения координат в II четверти: X (- ∞, 0) , Y (0, + ∞)')
    elif number == 3:
        print('Возможные значения координат в III четверти: X (- ∞, 0) , Y (- ∞, 0)')
    else:
        print('Возможные значения координат в IV четверти: X (0, + ∞) , Y (- ∞, 0')


print('Это программа, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).')
print('Введите номер координатной четверти: ')
GetRangeValue(GetNumberInt())
