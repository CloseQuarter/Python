# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 18:21:40 2017

@author: sanooj
"""

"""Stack - LIFO"""
class Stack:
     
    def __init__(self):
        self._data_store = []
        self.__top = -1
    
    def push(self,element):
        self._data_store.append(element)
        self.__top += 1 
        
    def pop(self):
        if len(self._data_store) > 0:
            self.__top -= 1 
            return self._data_store.pop()
        else:
            #should throw error
            print("Error: Trying to pop an empty Stack")
            pass
            
    def peek(self):
        if self.count() > 0:
            last_index = self.count() - 1
            return self._data_store[last_index]

    def isEmpty(self):
        return len(self._data_store) == 0        
    
    def count(self):
        return len(self._data_store)
    
    def top(self):
        if len(self._data_store) > 0:
            return self._data_store[0]
    
    
"""QUEUE - FIFO"""

"""Two Stacks Implementation"""
class Queue:
    def __init__(self):
        self.__main_data_store = Stack()
        self.__dequeue_helper_data_store = Stack()
        
    def isEmpty(self):
        return  (self.__main_data_store.isEmpty() 
                and self.__dequeue_helper_data_store.isEmpty())
    
    def size(self):
        return (self.__main_data_store.count() + 
                self.__dequeue_helper_data_store.count())
    
    def enqueue(self,element):
        self.__main_data_store.push(element)
        
    def peek(self):
        if self.__dequeue_helper_data_store.count() > 0:
            return self.__dequeue_helper_data_store.peek()
        
        elif self.__main_data_store.count() > 0:
            return self.__main_data_store.top()
        
        
    def dequeue(self):
        """
        1. 2 Stacks stack1 stack2
        2. check if stack 2 is empty
        3. if not - pop stack 2
        4. if stack 2 is empty
                move all elements from stack1 to stack2
        5. pop stack 2        
        """
        if (self.__main_data_store.count() == 0 and
            self.__dequeue_helper_data_store.count() == 0):
            return # nothing to dequeu
        
        if self.__dequeue_helper_data_store.count() == 0:
            #move stack1 to stack 2
            while not self.__main_data_store.isEmpty():
                popped_element = self.__main_data_store.pop()
                self.__dequeue_helper_data_store.push(popped_element)
                
            #pop stcak 2
        if self.__dequeue_helper_data_store.count() > 0:
            popped_element = self.__dequeue_helper_data_store.pop()
            return popped_element
            
            
queue = Queue()
for element in range(0,6):
    print("peek %s" %(queue.peek()))
    queue.enqueue(element)
    
print(queue._Queue__main_data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

queue.dequeue()

print("peek %s" %(queue.peek()))
print(queue._Queue__main_data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)


queue.enqueue(6)

print("peek %s" %(queue.peek()))
print(queue._Queue__main_data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

queue.dequeue()

print("peek %s" %(queue.peek()))
print(queue._Queue__main_data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

"""
Output

peek 0
peek 0
peek 0
peek 0
peek 0
[0, 1, 2, 3, 4, 5]
[]
peek 1
[]
[5, 4, 3, 2, 1]
peek 1
[6]
[5, 4, 3, 2, 1]
peek 2
[6]
[5, 4, 3, 2]
"""