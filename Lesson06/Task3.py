from math import sqrt
import os
os.system('cls')

print('Программа находит расстояние между двумя точками пространства(числа вводятся через пробел)')
list3 = [float(x) for x in input('Введите координаты точек x1, y1, x2, y2 через пробел: ').split(' ')]
# решение просто через формулу
print(round(float(sqrt(abs((list3[0]-list3[2])**2+(list3[1]-list3[3])**2))), 2))
# Решение через лямбда
get_distance_between_points = lambda x1, x2, y1, y2: round(float(sqrt(abs((x1-x2)**2+(y1-y2)**2))), 2)
print(get_distance_between_points(list3[0], list3[2], list3[1], list3[3]))