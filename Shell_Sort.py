# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 08:37:32 2022

@author: dcsem
"""
    
"""An implementation of Shell Sort algorithm, that takes
    O(n^2) time to sort the data, where n is the length of the input data.
    The algorithm may perform faster by changing the increments."""
    

def shellSort(alist):
    ''' Finds the number of sublists and them feeds them to gabInsertionSOrt()
        one at a time. When it is done with all of them, is splits the number of
        sublists in two and does the same again'''
    
    sublist_count = len(alist)//2
    
    while sublist_count > 0:
        
        for start_pos in range(sublist_count):
            gabInsertionSOrt(alist,start_pos,sublist_count)
            
        sublist_count = sublist_count//2
    print(alist)

def gabInsertionSOrt(alist,start,gap):
    '''Takes a sublist an itterate over it. In every iteration checks if the
        previous elements in the sublist are smaller. If that is the case, it moves
        all the elements with one position and puts the current element at the 
        positoin, where the previous one is not smaller.'''
    
    for i in range(start+gap,len(alist), gap):
        
        current = alist[i]
        pos = i
        
        while pos >= gap and alist[pos-gap] > current:
            
            alist[pos] = alist[pos-gap]
            pos = pos - gap
            
        alist[pos] = current
        


