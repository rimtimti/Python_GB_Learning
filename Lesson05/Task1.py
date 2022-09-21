import os
os.system('cls')

print('Это программа, которая удаляет из текста все слова, содержащие "абв".')
combination_of_letters = input('Введите комбинацию символов, имещюся в словах, которые надо удалить: ')
with open('less05_task1_start.txt', 'r', encoding='utf-8') as file1, open('less05_task1_del_text.txt', 'w', encoding='utf-8') as file2:
    for _ in file1.readlines():
        file2.writelines(" ".join(word for word in _.rstrip().split(' ') if not combination_of_letters in word)+'\n')
print('Посмотри файл: less05_task1_del_text.txt')

# Я тут не стал делать функцию, так как и так очень короткий код