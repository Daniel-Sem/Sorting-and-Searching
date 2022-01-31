# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 15:21:14 2022

@author: dcsem
"""

def insertion_sort(data):
    
    """An implementation of Insertion Sort algorithm, that takes
        O(n^2) time to sort the data, where n is the length of the input data."""
        
    for idx in range(1,len(data)):
        
        current_item = data[idx]
        pos = idx
        while pos > 0 and data[pos-1]>current_item:
            data[pos] = data[pos-1]
            pos = pos-1
        data[pos] = current_item
    print(data)
    
