"""
Name: YOUR NAME HERE
sortingFunctions.py
Description: Implementation of sorting algorithms.
"""

import time, random

def insertion_sort(list_to_sort):
    for i in range(1, len(list_to_sort)):
        j = i
        while j > 0 and list_to_sort[j - 1] > list_to_sort[j]:
            list_to_sort[j - 1], list_to_sort[j] = list_to_sort[j], list_to_sort[j - 1]
            j -= 1
    return list_to_sort
    

def bubble_sort(list_to_sort):
    """
    Sorts list_to_sort in ascending order using Bubble Sort.
    Modifies the list in-place and returns it.
    """
    n = len(list_to_sort)

    # Each pass pushes the largest remaining element to the end
    for i in range(n - 1):
        # Last i elements are already in final position
        for j in range(n - 1 - i):
            if list_to_sort[j] > list_to_sort[j + 1]:
                list_to_sort[j], list_to_sort[j + 1] = list_to_sort[j + 1], list_to_sort[j]

    return list_to_sort

def create_random_list(length):
    """ Returns a list of the given length with random values.
        Input: 
            length (int) - Desired length of the list """
    return random.sample(range(max(100, length)), length)
    
# Returns the length of time (in seconds) that it took
# for the function_to_run to sort a list of length list_length
def get_runtime(function_to_run, list_length):
    """ Returns the duration (in seconds) that it took for 
        function_to_run to sort a list of length list_length.
        Input: 
            function_to_run (function) - Name of the function
            list_length (int) - Length of the list to sort """
    # Create a new list to sort
    list_to_sort = create_random_list(list_length)
    # Get the time before running
    start_time = time.time()
    # Sort the given list
    function_to_run(list_to_sort)
    # Get the time after running
    end_time = time.time()
    # Return the difference
    return end_time - start_time

if __name__ == "__main__":
    for n in (100, 1000, 10000):
        print(f"Insertion sort ({n}):", get_runtime(insertion_sort, n))
    for n in (100, 1000, 10000):
        print(f"Bubble sort    ({n}):", get_runtime(bubble_sort, n))