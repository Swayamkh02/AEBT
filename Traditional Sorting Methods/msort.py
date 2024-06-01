# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 09:42:32 2023

@author: Swayam
"""

import random
import time

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 30000) for _ in range(10000)]

    # Measure the time taken to sort the array using Merge Sort
    start_time = time.time()
    sorted_arr = merge_sort(arr)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    # Print the first few sorted elements (for verification)
   # print("Sorted array (first 10 elements):", sorted_arr[:])

    # Print the total time taken for sorting
    print(f"Time taken for merge sorting: {elapsed_time:.6f} seconds")
