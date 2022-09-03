from math import sqrt


def GetNumberFloat():
    while type:
        number_float = input()
        try:
            number_float = float(number_float)
        except ValueError:
            print('Неверный ввод числа!!!')
        else:
            break
    return number_float


def GetDistanceBetweenPoints(x1_coordinate, y1_coordinate, x2_coordinate, y2_coordinate):
    return round(sqrt((x1_coordinate - x2_coordinate)**2 + (y1_coordinate - y2_coordinate)**2), 2)


print('Это программа, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.')
print('Введите координату x1: ')
x1 = GetNumberFloat()
print('Введите координату y1: ')
y1 = GetNumberFloat()
print('Введите координату x2: ')
x2 = GetNumberFloat()
print('Введите координату y2: ')
y2 = GetNumberFloat()
print(GetDistanceBetweenPoints(x1, y1, x2, y2))
