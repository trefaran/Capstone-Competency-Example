import random
random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

sorted_list = bubble_sort(random_list)
print(str(sorted_list) + " is the sorted list. (bubble sort)")
