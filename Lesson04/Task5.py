import defs
import os
os.system('cls')

print('Имеется файл: task5_start.txt, содержащий исходный текст.\nПрограмма реализует модуль RLE-сжатия и восстановления данных.')

with open('task5_start.txt', 'r', encoding='utf-8') as file1, open('task5_compression.txt', 'w', encoding='utf-8') as file2:
    for line in file1.readlines():
        file2.writelines(defs.text_compression(line)+'\n')
print('Посмотри файл task5_compression.txt')
with open('task5_compression.txt', 'r', encoding='utf-8') as file1, open('task5_decompression.txt', 'w', encoding='utf-8') as file2:
    for line in file1.readlines():
        file2.writelines(defs.text_decompression(line)+'\n')
print('Посмотри файл task5_decompression.txt')


# Проблема:      Если в исходном файле убрать пустую 4 строку, то 3-ю не сжимает, не могу понять почему

# Проблема:      Пробовал реализовать функцию открытия 1 файла, изменений и записи в другой. Внизу в файле defs.py.
#                Проблема в том, что в эту функцию нужно передавать 3-м аргументом РАЗНЫЕ другие функции.
#                Сдаю так и дальше думаю....
