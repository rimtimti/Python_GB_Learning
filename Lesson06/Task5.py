import os
os.system('cls')

print('Программа ищет произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
list5 = [float(x) for x in input('Введите список чисел через пробел: ').split(' ')]
print([round(list5[i]*list5[-i-1]) for i in range((len(list5)+1)//2)])