# -*- coding: utf-8 -*-
"""
Created on Sun Apr  1 21:29:30 2018

@author: sanooj
"""

def sequential_search(a_list, item):
    
    pos = 0
    found = False
    list_count = len(a_list)
    number_of_comparisons = 0
    
    while pos < list_count and not found:
        
        if a_list[pos] == item:
            found = True
            number_of_comparisons = \
            number_of_comparisons + 1
        
        else:
            pos = pos + 1
            number_of_comparisons = \
            number_of_comparisons + 1
        
        
        
    print("list_count %s" %(list_count)) 
    print("number_of_comparisons %s" %(number_of_comparisons))   
    
    return found

test_list = [1, 2, 32, 8, 17, 19, 42, 13, 0]
print(sequential_search(test_list, 3))
print(sequential_search(test_list, 13))

def ordered_sequential_search(a_list, item):
    
    pos = 0
    found = False
    stop = False
    list_count = len(a_list) 
    
    while pos < list_count and not found and stop:
        
        if a_list[pos] == item:
            found = True
        
        elif a_list[pos] > item:
            stop = True
        
        else:
            pos = pos + 1
            
    return found

test_list = [0, 1, 2, 8, 13, 17, 19, 32, 42,]
print(ordered_sequential_search(test_list, 3))
print(ordered_sequential_search(test_list, 13))