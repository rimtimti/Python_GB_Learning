print ('Это программа для проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат. \nПредикату можно заменить на понятие "бит". Должна получиться таблица истинности.')
print ('\nx\ty\tz\tresult')
print ('-------------------------------')
for x in True, False:
    for y in True, False:
        for z in True, False:
            if not (x or y or z) == (not x and not y and not z):
                result = True
            else:
                result = False
            print (f'{x}\t{y}\t{z}\t{result}')
print()

