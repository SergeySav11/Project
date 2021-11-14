
#Primes = list(map(int, input().split()))
#for i in range(len(Primes)):
    #if Primes[i] % 2 == 0:
    # print(Primes[i])


# Primes = list(map(int, input().split()))
# for i in range(len(Primes)):
#     if (i + 1) % 2 != 0:
#          print(Primes[i])


# Primes = list(map(int, input().split()))
# min = Primes[0]
# for i in range(len(Primes)):
#     if min > Primes[i]:
#         min = Primes[i]
# print(min)


# Primes = list(map(int, input().split()))
# sum = 0
# for i in range(len(Primes)):
#     if Primes[i] % 2 == 0:
#         sum = sum + Primes[i]
# print(sum)


# Primes = list(map(int, input().split()))
# sum = 0
# for i in range(1,len(Primes) -1):
#    if Primes[i] > Primes[ i+ 1] and Primes[i] > Primes[i -1]:
#        sum += 1
# print(sum)


# Primes = list(map(int, input().split()))
# max = 0
# for b in Primes:
#     if b % 2 == 0 and b > max:
#         max = b
# print(max)

# Primes = [1,3,2,5,4]
# def bubble_sort(arr):
#     def swap(i, j):
#         arr[i], arr[j] = arr[j], arr[i]
#
#     n = len(arr)
#     swapped = True
#
#     x = -1
#     while swapped:
#         swapped = False
#         x = x + 1
#         for i in range(1, n - x):
#             if arr[i - 1] > arr[i]:
#                 swap(i - 1, i)
#                 swapped = True
#     return arr
# print(bubble_sort((Primes)))


def selection_sort(arr):
    for i in range(len(arr)):
        minimum = i

        for j in range(i + 1, len(arr)):
            # Выбор наименьшего значения
            if arr[j] < arr[minimum]:
                minimum = j

        # Помещаем это перед отсортированным концом массива
        arr[minimum], arr[i] = arr[i], arr[minimum]

    return arr