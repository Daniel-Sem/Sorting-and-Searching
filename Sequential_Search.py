# -*- coding: utf-8 -*-
"""
Created on Fri Jan 14 10:22:47 2022

@author: dcsem
"""
    
def seq_search(items,val):
    
    """Implementation of a Sequential Search algorithm, that takes linear time
        O(n) in the worst case."""
        
    found = False
    count = 0
    
    while count < len(items) and not found:
        if items[count] == val:
            found = True
        else:
            count +=1
    
    return found


