n,m = list(map(int,input('Введите количество строк ит столбьцов: ').split()))
matrix = [list(map(int,input(f'Введите {i + 1} строку: ' ).split())) for i in range(n)]
for i in range(n):
    for g in range(m):
        matrix[i][g] *= matrix[i][g]
for i in matrix:
    print(*i)