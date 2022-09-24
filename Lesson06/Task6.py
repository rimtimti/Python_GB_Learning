import os
os.system('cls')
import defs

print('Программа формирует список из N членов последовательности: (-3) в степени N')
print([(-3)**x for x in range(defs.get_number_natural_int('Введите натуральное число N: '))])