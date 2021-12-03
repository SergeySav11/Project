import time
import random
from copy import deepcopy


def bubble_sort(nums):
    swap = True
    while swap:
        swap = False
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                nums[i],nums[i + 1] = nums[i + 1],nums[i]
                swap = True


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_index = i
        for b in range(i + 1,len(nums)):
            if nums[lowest_index] > nums[b]:
                lowest_index = b
        nums[lowest_index],nums[i] = nums[i],nums[lowest_index]


def quicksort(nums):
   if len(nums) <= 1:
       return nums
   else:
       q = random.choice(nums)
       s_nums = []
       m_nums = []
       e_nums = []
       for n in nums:
           if n < q:
               s_nums.append(n)
           elif n > q:
               m_nums.append(n)
           else:
               e_nums.append(n)
       return quicksort(s_nums) + e_nums + quicksort(m_nums)


def insertion_sort(nums):
    for i in range(1,len(nums)):
        x = nums[i]
        a = i - 1
        while a >= 0 and nums[a] > x:
            nums[a + 1] = nums[a]
            a -= 1
        nums[a + 1] = x


nums = random.sample(range(10001),10001)
copy = deepcopy(nums)
a = time.time()
bubble_sort(copy)
v = time.time()
print('bubble_sort',v - a)


copy = deepcopy(nums)
a = time.time()
quicksort(copy)
v = time.time()
print('quicksort',v - a)


copy = deepcopy(nums)
a = time.time()
insertion_sort(copy)
v = time.time()
print('insertion_sort',v - a)

copy = deepcopy(nums)
a = time.time()
selection_sort(copy)
v = time.time()
print( 'selection_sort', v - a)




