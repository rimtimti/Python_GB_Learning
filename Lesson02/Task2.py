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


def GetFactorialFromOweToN(number):
    array_factorials = [1]
    for i in range(1, number):
        array_factorials.append((i+1) * (array_factorials[i - 1]))
    return array_factorials


print('Это программа, которая принимает на вход целое число N и выдает факториал чисел от 0 до N.')
print(GetFactorialFromOweToN(GetNumberPositiveInt('Введите число: ')))
