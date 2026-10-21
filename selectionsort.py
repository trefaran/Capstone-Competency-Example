import random
import time

start = time.perf_counter()
random_list = [28, 22, 15, 55, 75, 37, 33, 44, 99, 90]
#random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)

def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

sorted_list = selection_sort(random_list)
print(str(sorted_list) + " is the sorted list. (selection sort) Time taken: " + str((time.perf_counter() - start) * 1000) + " milliseconds.")