# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 14:00:56 2022

@author: dcsem
"""

def short_bubble(data):
    
    """An implementation of Short Bubble sort algorithm, that takes
        O(n) = S(n) + C(n) time to find and item, where S(n) is the Number of Swaps
        and C(n) is the Number of Comparisons."""
    
    for not_done in range(len(data)-1,0,-1):
        exch = 0
        for j in range(not_done):
            if data[j] > data[j+1]:
                data[j], data[j+1] = data[j+1], data[j]
                exch +=1
                
        if exch == 0:
            break
        print(data)
    return data

