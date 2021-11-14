n = int(input('Введите количество строк и столбоцв: '))
matrix = []
for i in range(n):
    a = [0] * n
    matrix.append(a)
for i in matrix:
    print(*i,end= ' ')
for i in matrix:
    for g in i:
        print(g)
matrix = [list(map(int,input().split())) for i in range(n)]
for i in range(n):
    for g in range(n):
        print(matrix[g][i])