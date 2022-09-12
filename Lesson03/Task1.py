import defs

print('Это программа, которая задает список из нескольких целых чисел.\nЗатем ищет сумму элементов списка, стоящих на нечётной позиции.')
random_array = defs.CreateRandomArrayInt(defs.GetNumberPositiveInt('Введите целое положительное число необходимого количества элементов массива: '),
                                         defs.GetNumberInt('Введите целое число  минимально возможное в массиве: '),
                                         defs.GetNumberInt('Введите целое число максимально возможное в массиве: '))
print('Получился вот такой массив:')
print(random_array)
print(f'Сумма элементов списка, стоящих на нечётной позиции: {defs.GetSumElementsWithEvenOrOddIndex(random_array, 1)}')
