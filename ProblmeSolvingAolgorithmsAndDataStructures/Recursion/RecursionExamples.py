# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:45:13 2018

@author: sanooj
"""

"""
4.2.1 Calculating the Sum of a List of Numbers
"""

def list_sum(num_list):
    the_sum = 0
    
    for element in num_list:
        the_sum = the_sum + element
        
    return the_sum

print("sum %s" %(list_sum([1,3,5,7,9])))

def list_sum_recursion(num_list):
    
    print(num_list)
    
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum_recursion(num_list[1:])
    
print("sum %s" %(list_sum_recursion([1,3,5,7,9])))