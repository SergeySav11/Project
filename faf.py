'''
Изменяемые типы данных:списки словари и так далее,Неизменяемые типы данных:числа,строки и так далее
Структуры данных позвалают хранить информацию определенным образом а также они отличаются функцианалом
Двумерный список-список элементами которого являются списки
Матрица- это двумерный список у которого количество элементов во всех списках равно
Элементы матрцы-строки
Элементы строк образуют столбцы
Если количество строк и столбцов совпадают то матрциа называется квадратная
'''
a = [[1,0,2],[1,1,2],[0,0,2]]
for i in a:
    for b in i:
        if b == 1:
            print('|',end= '')
        elif b == 0:
            print(' ',end= '')
        else:
            print('o',end= '')
    print()
