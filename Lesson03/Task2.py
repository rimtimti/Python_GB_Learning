import defs

print('Это программа, которая задает список из нескольких целых чисел.\nЗатем ищет произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.')
random_array = defs.CreateRandomArrayInt(defs.GetNumberPositiveInt('Введите целое положительное число необходимого количества элементов массива: '),
                                         defs.GetNumberInt('Введите целое число  минимально возможное в массиве: '),
                                         defs.GetNumberInt('Введите целое число максимально возможное в массиве: '))
print('Получился вот такой массив:')
print(random_array)
print('Массив прозведений пар чисел такой:')
print(defs.GetMultiplicationPairsNumbersInArray(random_array))
