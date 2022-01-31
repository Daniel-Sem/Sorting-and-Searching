# -*- coding: utf-8 -*-
"""
Created on Wed Jan 19 11:50:54 2022

@author: dcsem
"""

def BubbleSort(the_list):
    
    """An implementation of Bubble Sort algorithm, that works in both directions
        simultaneously and takes O(n^2) time, where n is the length of the input list."""
    
    end = len(the_list)
    start = 0
    while end > start:
        for j in range(end):
            if j+1 < end:
                if the_list[j]>the_list[j+1]:
                    the_list[j],the_list[j+1] = the_list[j+1],the_list[j]
        end -=1
        for j in range(end,start,-1):
            if j-1 > start:
                if the_list[j]<the_list[j-1]:
                    the_list[j],the_list[j-1] = the_list[j-1],the_list[j]
        start+=1
        
    print(the_list)
    

