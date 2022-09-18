import defs
import os
os.system('cls')

print('Это программа, которая задает список из нескольких целых чисел.\nЗатем выдает список неповторяющихся элементов в порядке возрастания.')
random_array = defs.create_random_array_int(defs.get_number_positive_int('Введите целое положительное число необходимого количества элементов массива: '),
                                            defs.get_number_int('Введите целое число  минимально возможное в массиве: '),
                                            defs.get_number_int('Введите целое число максимально возможное в массиве: '))
print('Исходный массив: ')
print(random_array)
print('Уникальные значения этого массива: ')
print(defs.find_uniq_number(random_array))


