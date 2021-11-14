n,m = list(map(int,input('Введите количество строк ит столбьцов: ').split()))
#Генератор это конструкция которая позволяет заполнить список определённым образом
matrix = [list(map(int,input(f'Введите {i + 1} строку: ' ).split())) for i in range(n)]
matrix_2 = []
for i in range(n):
    a = [0] * m
    matrix_2.append(a)
def check(i,g):
    count = 0
    if g != m -1:
        if matrix[i][g + 1] != 0:
            count += 1
    if i != 0:
        if matrix[i - 1][g] != 0:
            count += 1
    return count
for i in range(n):
    for g in range(m):
        if matrix[i][g] != 0:
            matrix_2[i][g] = check (i,g)
for i in matrix_2:
    print(*i)
