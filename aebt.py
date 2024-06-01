# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 11:57:42 2023

@author: Swayam
"""
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import matplotlib.pyplot as plt
import random
import time


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BalancedTree:
    def __init__(self):
        self.root = None
        self.clf = DecisionTreeClassifier()

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else:
                self._insert_recursively(current_node.left, data)
        else:
            if current_node.right is None:
                current_node.right = Node(data)
            else:
                self._insert_recursively(current_node.right, data)

    def search(self, query):
        X, y = self._get_data()
        self.clf.fit(X, y)
        start_time = time.time()
        a=self.clf.predict(np.array([query]).reshape(-1, 1))[0]
        end_time = time.time()
        time_taken = end_time - start_time
        print("Time taken for AI searching=",time_taken," Seconds")
        search_data_array.append(time_taken)
        return a

    def sort(self):
        X, y = self._get_data()
        self.clf.fit(X, y)
        sorted_data = []
        start_t = time.time()
        self._in_order_traversal(self.root, sorted_data)
        end_t = time.time()
        time_taken = end_t - start_t
        print("Time taken for AI sorting=",time_taken," Seconds")
        sort_data_array.append(time_taken)
        return sorted_data

    def _in_order_traversal(self, node, sorted_data):
        if node is not None:
            self._in_order_traversal(node.left, sorted_data)
            prediction = self.clf.predict(np.array([node.data]).reshape(-1, 1))[0]
            sorted_data.append(prediction)
            self._in_order_traversal(node.right, sorted_data)

    def _get_data(self):
        X, y = [], []
        self._collect_data(self.root, X, y)
        return np.array(X).reshape(-1, 1), np.array(y)

    def _collect_data(self, node, X, y):
        if node is not None:
            self._collect_data(node.left, X, y)
            X.append([node.data])   
            y.append(node.data)
            self._collect_data(node.right, X, y)

if __name__ == '__main__':
    
    sort_data_array=[]
    search_data_array=[]
    sort_array_size=[]
    search_array_size=[]
    print("***** Data Operations Menu *****\n")
    #menu for data operations in the tree
    while 1>0:
        n=int(input("Enter the no of elements in the balanced tree :"))
        data= [random.randint(0,30000) for x in range(n)]
        tree = BalancedTree()
        for val in data:
            tree.insert(val)
        print("1.Sort\n2.Search\n3.Exit")
        count=int(input("Enter your choice:"))
        if count==1:
            sorted_data = tree.sort()
            sort_array_size.append(n)
            choice=0
            choice=int(input("Do you want to print the sorted array?:"))
            if choice:
                print("Sorted data:", sorted_data)
        elif count==2:
            #query=int(input("Enter the number to be searched:"))
            query = random.randint(0,30000) 
            search_array_size.append(n)
            result = tree.search(query)   
            if (result==query):
                print(f"Found element {query}")
            else:
                print(f"Element not found {query}\n")
                print(f"The nearest element to {query}: is {result}\n")
        elif count==3:
            break
        else:
            print("Enter a valid choice")
    #plotting the time calculated for the oparations
    print("***** Plotting Menu *****\n")
    choice=int(input("1.Sort Data\n2.Search Data\n3.Both data\n4.Exit\n"))
    if choice==1:
        plt.plot(sort_array_size,sort_data_array, marker='o', linestyle='-', color='b', label='Sorting Data')
        plt.show()
        plt.savefig('sort_plot.png')

    elif choice==2:
        plt.plot(search_array_size,search_data_array, marker='o', linestyle='-', color='r', label='Searching Data')
        plt.show()
        plt.savefig('search_plot.png')

    else:
        exit(0)
