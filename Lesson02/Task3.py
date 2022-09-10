def GetNumberPositiveFloat(input_string):
    try:
        number_float = int(input(input_string))
        if number_float < 0:
            print('Вы ввели отрицательное число!!!')
            return GetNumberPositiveFloat(input_string)
        else:
            return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberPositiveFloat(input_string)


def GetPalindrom(number):
    if (number == 196):
        return print('Навряд ли вы найдете палиндром 196 !!! =))))')
    count = 0
    while True:
        palindrom = round(float(str(round(number))[::-1]))
        if (palindrom != number):
            number += palindrom
            count += 1
        else:
            print (f'Палиндром этого числа - {palindrom}, после {count} шагов')
            break


print('Это программа, которая принимает на вход положительное целое число и находит его палиндром.')
GetPalindrom(GetNumberPositiveFloat('Введите число: '))

# Палиндромом называется слово, которое в обе стороны читается одинаково: "шалаш", "кабак".
# А еще есть палиндром числа - смысл также в том, чтобы число в обе стороны читалось одинаково, но есть одно "но".
# Если перевернутое число не равно исходному, то они складываются и проверяются на палиндром еще раз.
# Это происходит до тех пор, пока не будет найден палиндром.

# Здесь я использовал float, чтобы получить наибольшее вместилище для числа))