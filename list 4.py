a = [5,3,6,9]
for i in range(len(a)-1):
    if a[i] < a[i + 1]:
        print(a[i],end=' ')
print()
for i in range(len(a)-1):
    if a[i] > a[i + 1]:
        print(a[i],end=' ')
print()
for i in range(1,len(a)):
    if a[i] > a[i-1]:
        print(a[i],end=' ')
print()
matrix= [[4,5,6,8,9]]
for i in matrix:
    print(*i)
print()
a,b = list(map(int,input().split()))
sum = 0
matrix[a][b]
if a != 0:
    sum += 1
    if b != 0:
        sum += 1
    if b != len(matrix[0])- 1:
        sum += 1
if a != len(matrix) - 1:
    sum += 1
    if b != 0:
        sum += 1
    if b != len(matrix[0])-1:
        sum +=1
if b != 0:
    sum += 1
if b != len(matrix[0]) - 1:
    sum += 1

print(sum)