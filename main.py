from bubblesort import bubble_sort
from insertionsort import insertion_sort
from selectionsort import selection_sort
from quicksort import quick_sort
from mergesort import merge_sort
import random
import time

while(True):
    numElements = int(input("Enter the number of elements to sort: "))
    numTrials = int(input("Enter the number of trials to run: "))
    sortType = input("Enter the sorting algorithm to use (bubble, insertion, selection, quick, merge): ")
    start = time.perf_counter()
    for i in range(numTrials):
        random_list = [random.randint(1, 100) for i in range(numElements)]
        print(f"Trial {i+1}:")
        print("Unsorted list:", random_list)
        match sortType:
            case "bubble":
                sorted_list = bubble_sort(random_list)
            case "insertion":
                sorted_list = insertion_sort(random_list)
            case "selection":
                sorted_list = selection_sort(random_list)
            case "quick":
                sorted_list = quick_sort(random_list)
            case "merge":
                sorted_list = merge_sort(random_list)
            case _:
                print("Invalid sorting algorithm. Please try again.")
                continue
        print("Sorted list:", sorted_list)
    end = time.perf_counter()
    print(f"Time taken: {end - start} seconds")