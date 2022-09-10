from math import sqrt


def GetNumberFloat(input_string):
    try:
        number_float = float(input(input_string))
        return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberFloat(input_string)


def GetDistanceBetweenPoints(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate):
    return round(sqrt((x1_coordinate - x2_coordinate)**2 + (y1_coordinate - y2_coordinate)**2), 2)


print('Это программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
print(GetDistanceBetweenPoints(GetNumberFloat('Введите координату x1: '),
                               GetNumberFloat('Введите координату y1: '),
                               GetNumberFloat('Введите координату x2: '),
                               GetNumberFloat('Введите координату y2: ')))
