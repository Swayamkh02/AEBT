# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:35:22 2023

@author: Swayam"""
import random
import time

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 30000) for _ in range(10000)]

    # Measure the time taken to sort the array using Quick Sort
    start_time = time.time()
    sorted_arr = quick_sort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the first few sorted elements (for verification)
    #print("Sorted array (first 10 elements):", sorted_arr[:])

    # Print the total time taken for sorting
    print(f"Time taken for quick sorting: {elapsed_time:.6f} seconds")
