def GetNumberInt():
    while type:
        number_int = input()
        try:
            number_int = int(number_int)
        except ValueError:
            print('Неверный ввод числа!!!')
        else:
            break
    return number_int

def GetHoliday(number):
    if number < 1 or number > 7:
        print('Такого дня недели не существует!!!')
    elif number == 6 or number == 7:
        print('Ура! Это выходной!!!')
    else:
        print('Это рабочий день.')

print('Это программа, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.')
print('Введите номер дня недели: ')
GetHoliday(GetNumberInt())