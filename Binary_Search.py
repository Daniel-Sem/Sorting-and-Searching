# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 10:33:50 2022

@author: dcsem
"""

# Time complexity:
#     O(log n)

def bin_search(items, val):
    
    """Implementation of a Binary Search algorithm using pointers for first and
        last item in the sequence, that takes logarithmic time O(log n)."""
    
    first = 0
    last = len(items)-1
    found = False
    
    while first<=last and not found:
        
        mid_point = (first+last)//2
        
        if items[mid_point] == val:
            found = True
            
        else:
            if val < items[mid_point]:
                last = mid_point-1
            
            if val > items[mid_point]:
                first = mid_point+1
            
    return found


