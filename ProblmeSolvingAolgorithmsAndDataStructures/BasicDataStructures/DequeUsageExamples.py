# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 05:05:14 2018

@author: sanooj
"""

"""
Palindrome Checker
"""

from DataStructures.Deque import Deque

def pal_checker(a_string:str) -> bool:
    
    char_deque = Deque()
    print(char_deque.items)
    
    for char in a_string:
        print(char)
        char_deque.add_rear(char)
        
    print(a_string)
    print(char_deque.items)
    
    still_equal = True
    
    while char_deque.size() > 1 and still_equal:
        
        char_from_front = char_deque.remove_front()
        char_from_rear = char_deque.remove_rear()
        
        if char_from_front == char_from_rear:
            pass
        else:
            still_equal = False
        
    return still_equal
        

print(pal_checker("lsdkjfskf"))
print(pal_checker("radar"))