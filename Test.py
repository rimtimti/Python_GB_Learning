import os
from typing import List
from functools import reduce
os.system('cls')

# list2 = ['python', 'Action Script', 'C++', 'ColdFusion', 'Dart', 'Dylan', 'Eiffel', 'Objective-C', 'c#', 'Java', 'JavaScript']
# # list2 = filter(lambda x: not 'on' in x , list2)
# # list2 = map(str, list2)
# # list2 = list(filter(lambda x: not 'on' in x , list2))
# print(list(filter(lambda x: not 'on' in x , list2)))

# # print(list(map(filter(lambda x: not 'old' , list2), list2)))
# print(list(i for i in range(1, 21) if i % 2 == 0))
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
list2 = ['python', 'Action Script', 'C++', 'ColdFusion', 'Dart', 'Dylan', 'Eiffel', 'Objective-C', 'c#', 'Java', 'JavaScript']
def get_cortages_upper(list1: list, list2: list)-> List:
    '''
    Возвращает по одинаковому индексу список кортежей 1 списка и 2 списка, написанного большими буквами
    '''
    return [(list1[i-1], str(list2 [i-1]).upper()) for i in range (1, len(list1)+1)]

current_list = get_cortages_upper(list1, list2)
print(current_list)
# sec_list = reduce(lambda x: (ord(i) for i in list2[i].upper())[x], list2)
# print(sec_list)
# th_list = list(filter(lambda x: sum(ord(i) for i in list2.upper())%list1 == 0 in x , list2))
# print(th_list)

current_list = [(10,6,9),(0, 14, 16, 80),(8, 12, 30, 44)]
sorted_list = lambda x: (sorted(i) for i in x)
second_largest = lambda x, func: [y[len(y)-2] for y in func(x)]
result = second_largest(current_list, sorted_list)
print(result)