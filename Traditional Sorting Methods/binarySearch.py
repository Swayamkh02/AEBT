# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:50:38 2023

@author: Swayam
"""

import random
import time

def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

if __name__ == "__main__":
    # Generate a sorted list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = sorted([random.randint(1, 10000) for _ in range(10000)])
    
    # Choose a target element to search for (you can change this value)
    target_element = random.choice(arr)

    # Measure the time taken to perform a binary search
    start_time = time.time()
    result = binary_search(arr, target_element)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the array")

    # Print the total time taken for searching
    print(f"Time taken for searching: {elapsed_time:.6f} seconds")
