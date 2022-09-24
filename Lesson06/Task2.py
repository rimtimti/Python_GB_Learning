import os
os.system('cls')

print('Программа находит сумму чисел списка стоящих на нечетной позиции.')
list2 = [round(float(x), 2) for x in input('Введите список чисел через пробел: ').split(' ')]
print(round(sum(x for i, x in enumerate(list2) if i % 2 == 1),10))