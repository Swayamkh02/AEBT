# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:45:21 2023

@author: Swayam
"""

import random
import time

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # Flag to optimize the algorithm by checking if any swaps occurred
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap the elements if they are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swaps occurred, the array is already sorted
        if not swapped:
            break

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 30000) for _ in range(10000)]

    # Measure the time taken to sort the array using Bubble Sort
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the first few sorted elements (for verification)
    #print("Sorted array (first 10 elements):", arr[:])

    # Print the total time taken for sorting
    print(f"Time taken for bubble sorting: {elapsed_time:.6f} seconds")
