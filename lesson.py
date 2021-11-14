A = list(map(int, input().split()))
x = int(input())
i = len(A)
for b in range(len(A)):
    if A[b] < x:
        i = b
        break
print(i + 1)
print(*A[0:i],x,*A[i:len(A)])





    Primes = [4,5,6,7,8]
    sum = 0
    for b in range(len(Primes)):
        if Primes[b] != Primes[b + 1]:
            sum += 1
   print(sum)



Primes = []
print('Введите количество элементов')
col =int(input())
for b in range(col):
    print('Введите число ')
    Primes.append(input())
d = len(Primes)
print(d)
for i in range(len(Primes)):
    print(Primes[d])
    d = d -  1










