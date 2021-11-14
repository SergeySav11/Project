n,m = list(map(int,input('Введите количество строк ит столбьцов: ').split()))
#Генератор это конструкция которая позволяет заполнить список определённым образом
matrix = [list(map(int,input(f'Введите {i + 1} строку: ' ).split())) for i in range(n)]
for i in range(n):
    for g in range(m):
        matrix[i][g] += 1
for i in matrix:
    print(*i)
max = matrix[0][0]
for i in range(n):
    for g in range(m):
        if matrix[i][g] > max:
            max = matrix[i][g]
