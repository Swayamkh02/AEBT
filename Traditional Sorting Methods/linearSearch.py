# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 13:32:18 2023

@author: Swayam
"""

import random
import time

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

if __name__ == "__main__":
    # Generate a list of 5000 random elements
    random.seed(42)  # Seed for reproducibility
    arr = [random.randint(1, 10000) for _ in range(10000)]

    # Choose a target element to search for (you can change this value)
    target_element = 1024

    # Measure the time taken to perform a linear search
    start_time = time.time()
    result = linear_search(arr, target_element)
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time

    if result != -1:
        print(f"Element {target_element} found at index {result}")
    else:
        print(f"Element {target_element} not found in the array")

    # Print the total time taken for searching
    print(f"Time taken for searching: {elapsed_time:.6f} seconds")
