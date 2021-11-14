n,m = list(map(int,input('Введите количество строк ит столбьцов: ').split()))
matrix = [list(map(int,input(f'Введите {i + 1} строку: ' ).split())) for i in range(n)]
p = int(input('Введите число: '))
for i in range(n):
    for g in range(m):
        matrix[i][g] *= p
for i in matrix:
    print(*i)
min = matrix[0][0]
for i in range(n):
    for g in range(m):
        if matrix[i][g] < min:
            min = matrix[i][g]
print(min)
