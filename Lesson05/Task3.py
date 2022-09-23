from typing import List
import os
os.system('cls')

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list2 = ['python', 'Action Script', 'C++', 'ColdFusion', 'Dart', 'Dylan', 'Eiffel', 'Objective-C', 'c#', 'Java', 'JavaScript']

def get_cortages_upper(list1: list, list2: list)-> List:
    '''
    Возвращает по одинаковому индексу список кортежей 1 списка и 2 списка, написанного большими буквами
    '''
    return [(list1[i], str(list2 [i]).upper()) for i in range (0, len(list1))]

list3, list4 = [], []
for i in range (0, len(list1)):
    if sum(ord(i) for i in list2[i].upper())%list1[i] == 0:
        list3.append(sum(ord(i) for i in list2[i].upper()))
        list4.append(list2[i])

print(get_cortages_upper(list1, list2))
print(get_cortages_upper(list3, list4))

# Я, честно, пытался решить через filter и тд., но не смог, надо больше заданий каких-то попроще. Но, работает же )))
# Сдаю так..... Отстаю на целый семинар.