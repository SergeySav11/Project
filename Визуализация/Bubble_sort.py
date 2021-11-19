'''
Пузырьковая сортировка
Этот самый простой алгоритм сортировки который выполняет итерации(повторение в цикле) по списку, сравнивая элементы попарно и меняя их местами,
пока более крупные элементы не перестанут «всплывать»
до конца списка, а более мелкие элементы не будут оставаться «снизу».

Объяснение
Начнем со сравнения первых двух элементов списка. Если первый элемент больше второго, мы меняем их местами. Если они уже в нужном порядке, мы оставляем их как есть. Затем мы переходим
 к следующей паре элементов, сравниваем их значения и меняем местами при необходимости. Этот процесс продолжается до последней пары элементов в списке.

Достигнув конца списка, повторяем этот процесс для каждого элемента снова. Хотя это крайне неэффективно. Что если в массиве нужно сделать только одну замену?
Почему мы все еще повторяем, даже если список уже отсортирован? Получается нам нужно пройти список n^2 раза.

Очевидно, что для оптимизации алгоритма нам нужно остановить его, когда он закончит сортировку.

Откуда нам знать, что мы закончили сортировку? Если бы элементы были отсортированы, то нам не пришлось бы их менять местами. Таким образом, всякий раз, когда мы меняем элементы,
мы устанавливаем флаг в True, чтобы повторить процесс сортировки. Если перестановок не произошло, флаг останется False, и алгоритм остановится.
'''


def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i],nums[i + 1] = nums[i + 1],nums[i]
                swap = True
nums = [2,6,1,9,9,10,-5,-4]

bubble_sort(nums)
print(nums)