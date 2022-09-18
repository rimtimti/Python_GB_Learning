import defs

print('Это программа, которая задает список из нескольких вещественных чисел.\nЗатем ищет разницу между максимальным и минимальным значением дробной части элементов.')
random_array = defs.CreateRandomArrayFloat(defs.GetNumberPositiveInt('Введите целое положительное число необходимого количества элементов массива: '),
                                           defs.GetNumberFloat('Введите вещественное число  минимально возможное в массиве: '),
                                           defs.GetNumberFloat('Введите вещественное число максимально возможное в массиве: '),
                                           defs.GetNumberPositiveInt('Введите необходимое число знаков после запятой (max = 15!): '))
print('Получился вот такой массив:')
print(random_array)
print(f'Разница между максимальным и минимальным значением дробной части элементов: {defs.GetDiffBetweenMaxAndMinDecimalPart(random_array)}')

