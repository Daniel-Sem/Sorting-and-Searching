# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 20:13:45 2022

@author: dcsem
"""


def bin_search_rec(the_list, start, end,val):
    
    """An implementation of Binary Search algorithm with recursion, that takes
        logarithmic time O(log n)."""
    
    
    if end <= start:
        return False
    
    else:
        mid = (end + start)//2
        
        if the_list[mid] == val:
            return True
        
        elif val < the_list[mid]:
            return bin_search_rec(the_list, start, mid,val)
        
        else:
            return bin_search_rec(the_list, mid+1, end,val)
        
