import random
import time

start = time.perf_counter()
random_list = [28, 22, 15, 55, 75, 37, 33, 44, 99, 90]
#random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_list = merge_sort(random_list)
print(str(sorted_list) + " is the sorted list. (merge sort) Time taken: " + str((time.perf_counter() - start) * 1000) + " milliseconds.")