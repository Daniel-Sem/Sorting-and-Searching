# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 09:18:35 2022

@author: dcsem
"""

def mergeSort(alist):
    
    '''An implementation of Merge Sort algorithm, that takes O(n log n) time, where
        n is the length of the input data. The downside is it takes additional space
        for the recursion stack.
        
        Takes a list. Splits it recursively until the sublist are len of 1. The
        second step is to compare the elements of each sublist and to arrange
        them in the original list starting form the lowest to biggest.'''
    
    if len(alist)>1:
        
        start = 0
        mid = len(alist)//2
        end = len(alist)
        left_half = alist[start:mid]
        right_half = alist[mid:end]
    
        mergeSort(left_half)
        mergeSort(right_half)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(left_half) and j < len(right_half):
            
            if left_half[i] < right_half[j]:
                alist[k] = left_half[i]
                i+=1
            else:
                alist[k] = right_half[j]
                j+=1
            k+=1
            
        while i < len(left_half):
            alist[k] = left_half[i]
            i+=1
            k+=1
            
        while j < len(right_half):
            alist[k] = right_half[j]
            j+=1
            k+=1

    

