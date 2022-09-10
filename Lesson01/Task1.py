def GetNumberInt(input_string):
    try:
        number_int = int(input(input_string))
        return number_int
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberInt(input_string)


def GetHoliday(number):
    if number < 1 or number > 7:
        print('Такого дня недели не существует!!!')
    elif number == 6 or number == 7:
        print('Ура! Это выходной!!!')
    else:
        print('Это рабочий день.')


print('Это программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')
GetHoliday(GetNumberInt('Введите номер дня недели: '))
