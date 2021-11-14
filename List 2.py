# Primes = [4,5,6,7,8]
# sum = 1
# for b in range(len(Primes) - 1):
#     if Primes[b] != Primes[b + 1]:
#         sum += 1
# print(sum)

# Primes = input().split()
# print(Primes)
#
# Primes = map(int,input().split())
# print(Primes)
#
# Primes = list(map(int,input().split()))
# print(Primes)



# f = open("C:\INPUT.txt")
# o = open("C:\OUTPUT.txt","w")
# p = f.read()
# sum = 0
# print(len(p))
# b = 0
# for b in range(1,len(p)):
#     print(b)
#     if p[b] == '0':
#         sum += 1
#     else:
#         break
# print(sum)
# u = str(sum)
# o.write(u)
# o.close()
# f.close()


f = open("C:\INPUT.txt")
o = open("C:\OUTPUT.txt","w")
p = f.read()
u = 1
b= 0
Primes = []
Primes_2 = []
while p[b] != ' ':
    Primes.append(p[b])
    b += 1
while b  != len(p):
    Primes_2.append(p[b])
    b += 1
m = 1
sum = 0
for i in range(len(Primes)):
        print(len(Primes) - 1 - i,m,sum)
        sum = int(Primes[len(Primes) - 1 - i] )* m + sum
        m = m * 10
i = 1
sum_2 = 0
print(Primes_2)
m = 1
for i in range(len(Primes_2)- 1):
        print(len(Primes_2) - 1 - i,m,sum)
        sum_2= int(Primes_2[len(Primes_2) - 1 - i] )* m + sum_2
        m = m * 10
print(sum,sum_2)
for b in range(46340):
    if u % sum == 0 and u % sum_2 == 0:
        break
    u += 1
if u == 46341:
    print('Для данных чисел нету НОК')
print(u)





