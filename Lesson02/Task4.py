import datetime


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


def GetRandomIntFromTime(number1, number2):
    print(int((int(datetime.datetime.now().strftime('%f')) / 1000000) * (number2 - number1) + number1))


print('Это программа, которая принимает на вход минимальное и максимальное число диапазона (целое, положительное) и выдает случайное число из этого диапазона. \nРаботает от 0 до 999999')
GetRandomIntFromTime(GetNumberPositiveInt('Введите минимальное число диапазона: '),
                     GetNumberPositiveInt('Введите максимальное число диапазона: '))
