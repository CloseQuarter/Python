# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:05:19 2018

@author: sanooj
"""

"""
Linear data Structure
----------------------
2 ends - front and rear

Queue

1. push-down stack
2. adding happens at rear and removing happens at front
3. ie FIFO
4. ordering based on time
5. top the newest - base oldest
6. eg: Line
"""


class QueueADT(object):
    
    def enqueue(self,item):
        pass
    
    def dequeue(self) -> 'QueueADT':
        pass
    
    def is_empty(self):
        return True
    
    def size(self):
        return 0
    

class Queue(QueueADT):
    
    def __init__(self):
        self.items = []
        
    def is_empty(self) -> bool:
        return self.items == []
        
    def enqueue(self, item):
        self.items.insert(0,item)
        
    def dequeue(self) -> 'Queue':
        if not self.is_empty():
            return self.items.pop() #at bottom
        else:
            print("pop from empty list")
    
    def size(self):
        return len(self.items)
    

def trying_out_queue():
    q = Queue()
    print(q.items)
    q.enqueue("hello")
    print(q.items)
    q.enqueue("dog")
    print(q.items)
    q.enqueue(3)
    print(q.items)
    q.dequeue()
    print(q.items)
    for index,item in enumerate(q.items):
        print("%s %s" %(index,item))
    
trying_out_queue()
    