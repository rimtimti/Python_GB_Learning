import defs
import os
os.system('cls')

print('Имеется файл: task3_start.txt, содержащий фамилии студентов и их оценки.\nПрограмма просит число N и меняет на прописные буквы фамилии и имена тех студентов, которые имеют средний балл более N.\nПосмотри файл task3_finish.txt')
n = defs.get_number_float('Введите N: ')
with open('task3_start.txt', 'r', encoding='utf-8') as file1, open('task3_finish.txt', 'w', encoding='utf-8') as file2:
    lines = file1.readlines()
    for line in lines:
        if float(line.strip().split()[2]) > n:
            line = line.upper()
        file2.write(line)

# В задании средний балл - целое число. Я сделал, чтобы работало с дробными... причем с любыми N ))).
