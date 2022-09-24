import os
os.system('cls')
print('Программа вычисляет арифметическое выражение, заданное строкой.')

def check_correct_input(text: str) -> str:
    '''
    Проверяет правильность ввода арифметического выражения
    '''
    for symbol in text:
        if symbol.isalpha():
            print('Неправильный ввод: нужны числа')
            exit()
    for symbol in range(len(text)):
        count_left = 0
        count_right = 0
        if symbol == '(':
            count_left += 1
        if symbol == ')':
            count_right += 1
    if count_left != count_right:
        print("Некорректная запись скобок")    
        exit()
    if text[-1] == '+' or text[-1] == '-' or text[-1] == '*' or text[-1] == '/' or text[-1] == '(':
        print("Недостаточно числовых данных")
        exit()
    return text

def parse_into_numbers_and_signs(text: str) -> list:
    '''
    Разбирает арифметическое выражение в виде чисел и знаков
    '''
    result = []
    digit = ""
    for symbol in text:
        if symbol.isdigit() or symbol == '.':
            digit += symbol
        else:
            if digit:
                result.append(float(digit))
                digit = ""
            result.append(symbol)
        # else:
        #     if digit:
        #         result.append(float(digit))
        #     digit = ""
        #     result.append(symbol)
    # if digit:
    #     result.append(float(digit))
    if result[0] == '-':
        result.remove(result[0])
        result[0] = -1*result[0]
    return result

def calculator(array_numbers_and_sings: list) -> float:
    '''
    Вычисление выражений
    '''
    result = 0
    while '/' in array_numbers_and_sings:
        index = array_numbers_and_sings.index('/')
        result = array_numbers_and_sings[index - 1] / array_numbers_and_sings[index + 1]
        array_numbers_and_sings = array_numbers_and_sings[:index - 1] + [result] + array_numbers_and_sings[index + 2:]
    while '*' in array_numbers_and_sings:
        index = array_numbers_and_sings.index('*')
        result = array_numbers_and_sings[index - 1] * array_numbers_and_sings[index + 1]
        array_numbers_and_sings = array_numbers_and_sings[:index - 1] + [result] + array_numbers_and_sings[index + 2:]
    while '+' in array_numbers_and_sings:
        index = array_numbers_and_sings.index('+')
        result = array_numbers_and_sings[index - 1] + array_numbers_and_sings[index + 1]
        array_numbers_and_sings = array_numbers_and_sings[:index - 1] + [result] + array_numbers_and_sings[index + 2:]
    while '-' in array_numbers_and_sings:
        index = array_numbers_and_sings.index('-')
        result = array_numbers_and_sings[index - 1] - array_numbers_and_sings[index + 1]
        array_numbers_and_sings = array_numbers_and_sings[:index - 1] + [result] + array_numbers_and_sings[index + 2:]
    return result

def priority_brackets(array_numbers_and_sings: list) -> list:
    '''
    Вычисление выражений с учетом приоритета скобок
    '''
    while '(' in array_numbers_and_sings:
        close = array_numbers_and_sings.index(')')
        # temp = [y for x, y in zip(array_numbers_and_sings[:close], list(range(close-1))) if x == '(']
        open = [y for x, y in zip(array_numbers_and_sings[:close], list(range(close-1))) if x == '('][-1]        
        array_numbers_and_sings = array_numbers_and_sings[:open] + [calculator(array_numbers_and_sings[open + 1: close])] + array_numbers_and_sings[close + 1:]
    return array_numbers_and_sings

temp = ''.join(input('Введите математическое выражение: ').split())
result = priority_brackets(parse_into_numbers_and_signs(check_correct_input(temp)))
print(calculator(result))