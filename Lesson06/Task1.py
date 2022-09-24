import os
os.system('cls')
import defs

print('Программа определяет, присутствует ли в заданном списке строк, некоторое число.')
list1 = input('Введите список строк через пробел: ').split(' ')
number = defs.get_number_natural_int('Введите натуральное число N: ')
print(f'Указанное число есть?  {bool([char for word in list1 for char in word if char == str(number)])}') # ищет конкретное число в любой строке
print(f'Вообще какое-нибудь число есть?  {bool([word for word in list1 if word.isdigit()])}') # ищет любое число среди строк