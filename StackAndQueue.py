# -*- coding: utf-8 -*-
"""
Created on Tue Dec 12 23:10:33 2017

@author: sanooj
"""


"""Stack"""
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

    def isEmpty(self):
        return len(self._data_store) == 0        
    
    def peek(self):
        if not self.isEmpty():
            return self._data_store[len(self._data_store) - 1]
            
    
    def count(self):
        return len(self._data_store)


"""QUEUE"""

class Queue:
    def __init__(self):
        self.__top = -1
        self.__data_store = Stack()
        self.__dequeue_helper_data_store = Stack()
    
    def enqueue(self,element):
        self.__data_store.push(element)
    
    def dequeue(self):
       
        current_pop = None
        
        print(self.__data_store.isEmpty())
        
        while (self.__data_store.isEmpty() == False):
            if self.__data_store.count() == 1:
                return self.__data_store.pop()
            else:
                while not self.__data_store.isEmpty():
                    ## Move all elements to another stack except the first one
                    ## When the lopp recahes the last elemnt .. ie.. the first element in the datastore
                    ## as stach pops from bottom
                    ## return that
                    current_pop = self.__data_store.pop()
                    self.__dequeue_helper_data_store.push(current_pop)
                    
                    #print("__data_store AFTER POP %s" %(self.__data_store._data_store))
                    #print("__data_store count %s" %(self.__data_store.count()))
                    
                    #first element
                    if self.__data_store.count() == 1:
                        #print("__data_store AFTER POP at count == 1 %s" %(self.__data_store._data_store))
                        current_pop = self.__data_store.pop()
                        #print("__data_store AFTER  final POP %s" %(self.__data_store._data_store))
        
        #Re-populate the dataStore                
        while not self.__dequeue_helper_data_store.isEmpty():
            popped_value  = self.__dequeue_helper_data_store.pop()
            print("popped %s" %(popped_value))
            self.__data_store.push(popped_value)
            print("__data_store %s" %(self.__data_store._data_store))
                        
        return current_pop
    
    def dequeue_alt_fast(self):
        """
        1. push all items to stack 2 if it is empty
        2. pop the stack2
        3. since elements get added in reverse
        """
        
        #check if stacks are empty
        if self.__data_store.isEmpty() and self.__dequeue_helper_data_store.isEmpty():
            return
        
        # if stack 2 is empty
        if self.__dequeue_helper_data_store.isEmpty():
            ##move items from stack1 to stack 2
            while not self.__data_store.isEmpty():
                popped_item = self.__data_store.pop()
                self.__dequeue_helper_data_store.push(popped_item)
    
        if not self.__dequeue_helper_data_store.isEmpty():
            popped_item = self.__dequeue_helper_data_store.pop()
            return popped_item
            
    def isEmpty(self):
        return self.__data_store.isEmpty() and self.__dequeue_helper_data_store.isEmpty()
    
    def peek(self):
        return self.__dequeue_helper_data_store.peek()
    
    def show_all(self):
        while not self.__data_store.isEmpty():
            current_pop = self.__data_store.pop()
            self.__dequeue_helper_data_store.push(current_pop)
            
    def size(self):
        return self.__data_store.count() + self.__dequeue_helper_data_store.count()        
                
            
queue = Queue()
for element in range(0,6):
    print("peek %s" %(queue.peek()))
    queue.enqueue(element)

#print(queue.peek())

#print(queue._Queue__peekCandidate)

print(queue._Queue__data_store._data_store)

print("dequeue")
print(queue.dequeue_alt_fast())

print(queue._Queue__data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

print("enqueue")
queue.enqueue(9)
print("peek %s" %(queue.peek()))
queue.enqueue(10) 
print("peek %s" %(queue.peek()))
queue.enqueue(11)
print("peek %s" %(queue.peek()))

print(queue._Queue__data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)


print("2nd dequeue")
print(queue.dequeue_alt_fast())
print("peek %s" %(queue.peek()))

print(queue._Queue__data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

while not queue.isEmpty():
    print("queue.size()")
    print(queue.size())
    print(queue._Queue__data_store._data_store)    
    print(queue._Queue__dequeue_helper_data_store._data_store)    
    print("deq %s" %(queue.dequeue_alt_fast()))

print("after looping")
print(queue._Queue__data_store._data_store)
print(queue._Queue__dequeue_helper_data_store._data_store)

def queue_dequeue(push_stack,pop_stack,element):
    if push_stack.isEmpty() and pop_stack.isEmpty():
        pass
    
    if pop_stack.isEmpty():
        while not push_stack.isEmpty():
            popped_item = push_stack.pop()
            pop_stack.push(popped_item)
    
    final_pop = push_stack.pop()

    return final_pop        
    
    