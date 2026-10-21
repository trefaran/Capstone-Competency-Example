import random
random_list = [random.randint(1, 100) for i in range(10)]
print(random_list)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

sorted_list = insertion_sort(random_list)
print(sorted_list)