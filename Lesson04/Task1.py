import defs
import os
os.system('cls')

print('Это программа, которая принимает на вход наруральное число и выдает список простых множителей этого числа.')
print(defs.get_simple_number_from_array(defs.get_multipliers_number(defs.get_number_natural_int('Введите целое число: '))))
