from random import randint
from typing import List


def get_number_natural_int(input_string):
    try:
        number_int = int(input(input_string))
        if number_int <= 0:
            print('Вы ввели отрицательное число или ноль!!!')
            return get_number_natural_int(input_string)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_number_natural_int(input_string)


def get_number_float(input_string):
    try:
        number_float = float(input(input_string))
        return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_number_float(input_string)


def get_number_positive_int(input_string):
    try:
        number_int = int(input(input_string))
        if number_int < 0:
            print('Вы ввели отрицательное число!!!')
            return get_number_positive_int(input_string)
        else:
            return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_number_positive_int(input_string)


def get_number_int(input_string: str) -> int:
    '''
    Просит у пользователя ввести целое число и проверяет его
    '''
    try:
        number_int = int(input(input_string))
        return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return get_number_int(input_string)


def create_random_array_int(size_array: int, min_element: int, max_element: int) -> List[int]:
    '''
    Генерирует массив из N целых чисел от min до max
    '''
    list_int = []
    for i in range(size_array):
        list_int.append(randint(min_element, max_element))
    return list_int


def get_multipliers_number(number: int) -> List[int]:
    '''
    Выдает все множители числа
    '''
    array_multipliers = []
    for i in range(1, number+1):
        if number % i == 0:
            array_multipliers.append(i)
            number /= i
    return array_multipliers


def get_simple_number_from_array(array: list[int]) -> List[int]:
    '''
    Выдает простые числа
    '''
    if array == [1]:
        print('Число 1 не имеет простых делителей и не является ни простым, ни составным числом.')
        return
    array_simple_number = []
    for i in array:
        if get_multipliers_number(i) == [1, i]:
            array_simple_number.append(i)
    return array_simple_number


def find_uniq_number(array: list[int]) -> List[int]:
    '''
    Ищет уникальные значения и сортирует их в порядке возрастания
    '''
    array_uniq = []
    for i in array:
        if i not in array_uniq:
            array_uniq.append(i)
    return sorted(array_uniq)


def caesar_encryption(text: str, number: int) -> str:
    '''
    Кодирует текст шифром Цезаря по ключу
    '''
    alphabet, cipher_text = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя', ''
    for char in text.lower():
        if char in alphabet:
            cipher_text += alphabet[(alphabet.find(char) + number) % len(alphabet)]
        else:
            cipher_text += char
    return cipher_text.capitalize()


def text_compression(text: str) -> str:
    '''
    Сжимает текст по RLE-алгоритму
    '''
    text += ' '
    compress, count = '', 1
    for i in range(len(text)-1):
        if i <= (len(text)+1):
            if text[i] == text[i + 1]:
                count += 1
            else:
                compress += str(count)+str(text[i])
                count = 1
    return compress


def text_decompression(text: str) -> str:
    '''
    Восстанавливает текст из RLE-сжатия
    '''
    text += ' '
    decompress, count = '', ''
    for i in range(len(text)-1):
        if i <= (len(text)+1):
            if text[i].isdigit():
                count += text[i]
            else:
                decompress += int(count) * text[i]
                count = ''
    return decompress


# def take_information_from_file_modify_and_write_to_another(text1: str, text2: str, <function>) -> File:
#     '''
#     Берет информацию из одного файла, изменяет и записывает в другой файл
#     '''
#     with open(text1, 'r', encoding='utf-8') as file1, open(text2, 'w', encoding='utf-8') as file2:
#         lines = file1.readlines()
#         for line in lines:
#             file2.writelines(<function>+'\n')