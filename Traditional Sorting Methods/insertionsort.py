# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 10:02:01 2023

@author: Swayam
"""

import random
import time

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 30000) for _ in range(15000)]

    # Measure the time taken to sort the array using Insertion Sort
    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the first few sorted elements (for verification)
    #print("Sorted array (first 10 elements):", arr[:])

    # Print the total time taken for sorting
    print(f"Time taken for insertion sorting: {elapsed_time:.6f} seconds")
