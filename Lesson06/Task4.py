import os
os.system('cls')

print('Программа определяет, позицию второго вхождения строки в списке либо сообщить, что её нет.')
list4 = input('Введите список строк через пробел: ').split(' ')
print(list4)
find_str = input('Введите какую строку вы ищете в этом списке: ')
print([i for i in range(len(list4)) if list4[i] == find_str] [1:2])