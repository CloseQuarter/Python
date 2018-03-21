# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 03:37:55 2018

@author: sanooj
"""

"""
Deque 

1. has two end.. rear and end
2. items can be aded or removed from both ends
"""

from typing import TypeVar, Generic

T = TypeVar("T")

class DequeADT(Generic[T]):
    
    def __init__(self):
        pass
    
    def add_front(self,item:T):
        pass
    
    def add_rear(self,item:T):
        pass
    
    def remove_front(self) -> T:
        return None
    
    def remove_rear(self) -> T:
        return None
    
    def is_empty(self) -> bool:
        return True
        
    def size(self) -> int:
        return 0
    
    
class Deque(DequeADT):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self) -> bool:
        return self.items == []
    
    def add_front(self, item:T):
        self.items.append(item)
        
    def add_rear(self, item:T):
        self.items.insert(0,item)
        
    def remove_front(self) -> T:
        return self.items.pop()
        
    def remove_rear(self) -> T:
        return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    
    