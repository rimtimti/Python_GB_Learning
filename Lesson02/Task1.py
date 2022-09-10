from decimal import Decimal


def GetNumberDecimal(input_string):
    try:
        number_float = Decimal(input(input_string))
        return number_float
    except ValueError:
        print('Неверный ввод числа!!!')
        return GetNumberDecimal(input_string)

# чисто математическое решение, больше кода (
# def GetSumNumbersInNumber(number):
#     sum_num = 0
#     while (number - number // 1) > 0:
#         number *= 10
#     while number > 0:
#         sum_num += number % 10
#         number //= 10
#     return round(sum_num)


def GetSumNumbersInNumber(number):
    str_number = str(number)
    sum_num = 0
    for i in range(len(str_number)):
        if str_number[i].isdigit():
            sum_num += int(str_number[i])
    return sum_num


print('Это программа, которая принимает на вход вещественное число и показывает сумму его цифр.')
print(GetSumNumbersInNumber(abs(GetNumberDecimal('Введите число: '))))


# Здесь я использовал Decimal, чтобы число было более предсакзуемым, чем float))