from typing import List
import os
os.system('cls')


list2 = ['python', 'Action Script', 'C++', 'ColdFusion', 'Dart', 'Dylan', 'Eiffel', 'Objective-C', 'c#', 'Java', 'JavaScript']


def divisibility_sum_of_letters_to_number(array_numder_and_text):
    filtered_list = []
    for number, word in array_numder_and_text:
        if sum(ord(chr) for chr in word) % number == 0:
            filtered_list.append((sum(ord(i) for i in word), word))
    return filtered_list

print(list(enumerate(list(map(lambda language: language.upper(), list2)), 1)))
print(divisibility_sum_of_letters_to_number(list(enumerate(list(map(lambda language: language.upper(), list2)), 1))))
