# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:11:03 2022

@author: dcsem
"""

def select_sort(data):
    
    """An implementation of Selecttion Sort algorithm, that takes
        O(n^2) time to sort the data, where n is the length of the input data."""
    
    for passed in range(len(data), 0, -1):
        
        biggest_idx = 0
        for i in range(1,passed):
                        
            if data[i] > data[biggest_idx]:
                biggest_idx = i
               
        data[biggest_idx], data[passed-1]= data[passed-1], data[biggest_idx]
    print(data)
    

