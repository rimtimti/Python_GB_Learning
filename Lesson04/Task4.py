import defs
import os
os.system('cls')

print('Имеется файл: task4_start.txt, содержащий исходный текст.\nПрограмма просит ввести ключ и записывает в файл шифрованный текст шифром Цезаря.')
key = defs.get_number_int('Введите целое число - ключ шифра: ')
with open('task4_start.txt', 'r', encoding='utf-8') as file1, open('task4_cipher.txt', 'w', encoding='utf-8') as file2:
    for line in file1.readlines():
        file2.writelines(defs.caesar_encryption(line, key))
print('Посмотри файл task4_cipher.txt')
print()
key = -1*defs.get_number_int('Для обратной расшифровкив введите ключ шифра: ')
with open('task4_cipher.txt', 'r', encoding='utf-8') as file1, open('task4_decipher.txt', 'w', encoding='utf-8') as file2:
    for line in file1.readlines():
        file2.writelines(defs.caesar_encryption(line, key))
print('Посмотри файл task4_decipher.txt')
