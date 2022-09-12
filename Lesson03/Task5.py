import defs

print('Это программа, которая принимает на вход положительное целое число и составляет список чисел Фибоначчи, в том числе для отрицательных индексов.')
num = defs.GetNumberPositiveInt('Введите положительное целое число: ')
print(defs.GetNegativeFibonacci(num) + defs.GetFibonacci(num))
