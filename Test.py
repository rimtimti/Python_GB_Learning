import os
os.system('cls')

array_numbers_and_sings = [-3.0, '*', '(', 2.0, '+', '(', '(', 5.0, '-', 3.0, ')', '*', '(', 16.0, '-', 14.0, ')', ')', ')', '/', '(', 3.0, '+', 3.0, ')']
dictionary_sings = {1:'/', 2:'*', 3:'+', 4:'-'}
result = 0
while dictionary_sings in array_numbers_and_sings:
    for i in range(array_numbers_and_sings):
        index = array_numbers_and_sings.index(dictionary_sings)
        if dictionary_sings[1]:
            result = array_numbers_and_sings[index - 1] / array_numbers_and_sings[index + 1]
        if dictionary_sings[2]:
            result = array_numbers_and_sings[index - 1] * array_numbers_and_sings[index + 1]
        if dictionary_sings[3]:
            result = array_numbers_and_sings[index - 1] + array_numbers_and_sings[index + 1]
        if dictionary_sings[4]:
            result = array_numbers_and_sings[index - 1] - array_numbers_and_sings[index + 1]
    array_numbers_and_sings = array_numbers_and_sings[:index - 1] + [result] + array_numbers_and_sings[index + 2:]
print(result)