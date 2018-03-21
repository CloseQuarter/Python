# -*- coding: utf-8 -*-
"""
Created on Sun Feb  4 13:46:10 2018

@author: sanooj
"""

"""

Linear data Structure
----------------------
2 ends - top and bobasettom

Stack

1. push-down stack
2. adding and removing happens at the same end
3. ie LIFO
4. ordering based on time
5. top the newest - base oldest
6. can be used to reverse objects
"""

class StackADT:
    
    def push(self,item):
        pass
    
    def pop(self):
        return None
    
    def peek(self):
        return None
    
    def is_empty(self):
        return 0
    
    def size(self):
        return 0
    
"""
Stack Implementation

// top at the end of the list
"""
class Stack(StackADT):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
        
    def peek(self):
        if self.is_empty():
            return None
        else:
            count = len(self.items)
            return self.items[count - 1]
        
    def size(self):
        return len(self.items)
    
    def debug_print(self):
        print("items -> %s" %(self.items))
    

def testingAStack():
    s = Stack()
    print(s.is_empty())
    s.push(4)
    s.push('dog')
    s.debug_print()
    print(s.peek())
    s.debug_print()
    s.push(True)
    s.debug_print()
    print(s.size())
    print(s.is_empty())
    s.push(8.4)
    s.debug_print()
    print(s.pop())
    s.debug_print()
    print(s.pop())
    s.debug_print()
    print(s.size())
    
testingAStack()

"""
# top at the end of the list

push to index 0
pop at index 0

"""
def testingStackAtTopOLlist():
    
    class Stack(StackADT):
    
        def __init__(self):
            self.items = []
            
        def is_empty(self):
            return self.items == []
        
        def push(self,item):
            self.items.insert(0,item)
            
        def pop(self):
            return self.items.pop(0)
            
        def peek(self):
            return self.items[0]
            
        def size(self):
            return len(self.items)
        
        def debug_print(self):
            print("items -> %s" %(self.items))
        
    def testingAStack():
            s = Stack()
            print(s.is_empty())
            s.push('hello')
            s.push('true')
            print(s.pop())
            
    testingAStack()

testingStackAtTopOLlist()