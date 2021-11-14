#Заполнение матрицы нулями
matrix = []
for i in range(n):
    a = [0] * m
    matrix.append(a)
#Вывод матрицы на экран
for i in matrix:
    print(*i)
#Перебор элементов матрциы по значению
for i in matrix:
    for g in i:
        print(g)
#Перебор элементов матрицы по индексу(предпочтительный вариант)
for i in range(n):
    for g in range(m):
        print(matrix[i][g])
#Изменение элемента матрицы
matrix[i][g] = int(input())
#Заполнение матрицы с клавиатуры
matrix = [list(map(int,input().split())) for i in range(n)]


