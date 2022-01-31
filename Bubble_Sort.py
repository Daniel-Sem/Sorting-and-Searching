# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 13:43:17 2022

@author: dcsem
"""

def bubble_sort(data):
    
    """An implementation of Bubble Sort algorithm, that takes
        O(n^2) time, where n is the length of the input data."""
    
    for not_done in range(len(data)-1,0,-1):
        for j in range(not_done):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]

    return data


