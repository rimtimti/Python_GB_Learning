from random import randint, randrange, uniform
from typing import List, Union


def GetNumberInt(input_string: str) -> int:
    '''
    Просит у пользователя ввести целое число и проверяет его
    '''
    try:
        number_int = int(input(input_string))
        return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberInt(input_string)

def GetNumberPositiveInt(input_string):
    try:
        number_int = int(input(input_string))
        if number_int < 0:
            print('Вы ввели отрицательное число!!!')
            return GetNumberPositiveInt(input_string)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberPositiveInt(input_string)

def GetNumberFloat(input_string):
    try:
        number_float = float(input(input_string))
        return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberFloat(input_string)

def GetNumberPositiveInt(input_string: str) -> int:
    '''
    Просит у пользователя ввести целое положительное число и проверяет его
    '''
    try:
        number_int = int(input(input_string))
        if number_int < 0:
            print('Вы ввели отрицательное число!!!')
            return GetNumberPositiveInt(input_string)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberPositiveInt(input_string)

def CreateRandomArrayInt(size_array: int, min_element: int, max_element: int) -> List[int]:
    '''
    Генерирует массив из N целых чисел от min до max
    '''
    list_int = []
    for i in range(size_array):
        list_int.append(randint(min_element, max_element))
    return list_int

def CreateRandomArrayFloat(size_array: int, min_element: Union[int, float], max_element: Union[int, float], number_of_decimal_places: int) -> List[Union[int, float]]:
    '''
    Генерирует массив из N вещественных чисел от min до max c X знаков после запятой
    '''
    list_float = []
    for i in range(size_array):
        list_float.append(round(uniform(min_element, max_element), number_of_decimal_places))
    return list_float

def GetSumElementsWithEvenOrOddIndex(array: list, number: int) -> Union[int, float]:
    '''
    Принимает массив и находит сумму элементов на четных (number=0) или нечетных (number=1) позициях
    '''
    sum_elements = 0
    for i in range(len(array)):
        if i % 2 == number:
            sum_elements += array[i]
    return sum_elements

def GetMultiplicationPairsNumbersInArray (array: list [Union[int, float]]) -> List [Union[int, float]]:
    '''
    Ищет произведение пар чисел списка.\n Парой считаем первый и последний элемент, второй и предпоследний и т.д.
    '''
    multiplication_array = []
    for i in range((len(array)+1)//2):
        multiplication_array.append(array[i] * array[ (- i - 1)])
    return multiplication_array

def GetDiffBetweenMaxAndMinDecimalPart(array: list) -> float:
    '''
    Ищет разницу между максимальным и минимальным значением дробной части элементов.
    '''
    min_decimal_part = 1
    max_decimal_part = 0
    for i in range(len(array)):
        if array[i]%1 < min_decimal_part:
            min_decimal_part = array[i]%1
        if array[i]%1 > max_decimal_part:
            max_decimal_part = array[i]%1
    return round((max_decimal_part - min_decimal_part), 16)

def GetFibonacci(number: int) -> List[int]:
    '''
    Выдает числа Фибоначчи от 1 до N
    '''
    fibonacci = []
    for i in range (0, number):
        if i in [0,1]:
            fibonacci.append(1)
        else:
            fibonacci.append((fibonacci[i-1]+fibonacci[i-2]))
    return fibonacci

def GetNegativeFibonacci(number: int) -> List[int]:
    '''
    Выдает отрицательные числа Фибоначчи от -N до 0
    '''
    negative_fibonacci = [0, 1]
    for i in range (2, number+1):
        negative_fibonacci.append((negative_fibonacci[i-2]-negative_fibonacci[i-1]))
    return list(reversed(negative_fibonacci))

def GetBin(number: int) -> int:
    '''
    Выдает десятичное число в двоичной системе счисления
    '''
    bin_number = ''
    while number > 0:
        bin_number += str(number %2)
        number //= 2
    else:
        return int(str(bin_number)[::-1])
