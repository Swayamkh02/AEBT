# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:50:11 2023

@author: Swayam
"""

import random
import time

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i

        # Find the minimum element in the remaining unsorted portion of the array
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the minimum element with the first element of the unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 30000) for _ in range(10000)]

    # Measure the time taken to sort the array using Selection Sort
    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the first few sorted elements (for verification)
    #print("Sorted array (first 10 elements):", arr[:])

    # Print the total time taken for sorting
    print(f"Time taken for selection sorting: {elapsed_time:.6f} seconds")
