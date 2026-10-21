import random
random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

sorted_list = quick_sort(random_list)
print(str(sorted_list) + " is the sorted list. (quick sort)")