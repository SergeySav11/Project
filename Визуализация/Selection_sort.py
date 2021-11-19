'''
Сортировка выбором
Этот алгоритм сегментирует список на две части: отсортированные и несортированные. Он постоянно удаляет наименьший элемент из несортированного сегмента списка
и добавляет его в отсортированный сегмент.

Объяснение
На практике нам не нужно создавать новый список для отсортированных элементов, мы будет обрабатывать крайнюю левую часть списка как отсортированный сегмент.
Затем мы ищем во всем списке наименьший элемент и меняем его на первый элемент.

Теперь мы знаем, что первый элемент списка отсортирован, мы получаем наименьший элемент из оставшихся элементов и заменяем его вторым элементом.
Это повторяется до тех пор, пока последний элемент списка не станет оставшимся элементом для изучения.
'''


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_index = i
        for b in range(i + 1,len(nums)):
            if nums[lowest_index] > nums[b]:
                lowest_index = b
        nums[lowest_index],nums[i] = nums[i],nums[lowest_index]


nums = [2,6,1,9,9,10,-5,-4]
selection_sort(nums)
print(nums)
