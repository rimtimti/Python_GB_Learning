def GetNumberFloat(input_string):
    try:
        number_float = float(input(input_string))
        return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberFloat(input_string)


def GetPointLocation(x_coordinate, y_coordinate):
    if x_coordinate == 0 and y_coordinate == 0:
        print('Это точка пересечения координат !')
    elif x_coordinate == 0:
        print('Эта точка находится на оси Y !')
    elif y_coordinate == 0:
        print('Эта точка находится на оси X !')
    elif x_coordinate > 0 and y_coordinate > 0:
        print('Эта точка находится в I координатной четверти.')
    elif x_coordinate < 0 and y_coordinate > 0:
        print('Эта точка находится в II координатной четверти.')
    elif x_coordinate < 0 and y_coordinate < 0:
        print('Эта точка находится в III координатной четверти.')
    else:
        print('Эта точка находится в IV координатной четверти.')


print('Это программа, которая принимает на вход координаты точки (X и Y), и выдаёт номер четверти плоскости, в которой она находится, или на какой оси она находится.')
GetPointLocation(GetNumberFloat('Введите координату X: '),
                 GetNumberFloat('Введите координату Y: '))
