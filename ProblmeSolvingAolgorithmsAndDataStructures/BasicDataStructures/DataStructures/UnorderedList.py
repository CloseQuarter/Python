# -*- coding: utf-8 -*-
"""
Created on Mon Mar 12 22:41:26 2018

@author: sanooj
"""

"""
Unordered list with a Linked list
"""

class ListADT(object):
    
    def __init__(self):
        pass
    
    def add(self, item):
        pass
    
    def remove(self, item):
        pass
    
    def search(self, item):
        pass
    
    def is_empty(self):
        return True
    
    def size(self):
        return 0
    
    def append(self, item):
        pass
    
    def index(self, item):
        return None
    
    def insert(self, pos, item):
        pass
     
    def pop(self, pos):
        return None
    
"""
first item called Head
"""

class Node:
    
    def __init__(self, init_data):
        self.data = init_data
        self.next = None
        
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self, new_data):
        self.data = new_data
        
    def set_next(self, new_next):
        self.next = new_next
        
class UnOrderedList(ListADT):
    
    def __init__(self):
        self.head = None
        #adding tail
        self.tail = None
        
    def is_empty(self):
        return self.head == None
    
    """
    Add to top by replacing head
    """
    def add(self, item):
        
        #new node
        node =  Node(item)
        
        #set head as next
        node.set_next(self.head)
        
        self.head = node
        
        if self.tail == None:
            self.tail = node.get_next()
    
    def size(self):
        
        count = 0
        current_node = self.head
        
        while current_node != None:
            count = count + 1
            current_node = current_node.get_next()
            
        return count
    
    def search(self, item):
        
        current_node = self.head
        found = False
        found_node = None
        
        while current_node != None and not found:
          
            #get data
            data = current_node.get_data()
            print(data)
            
            #comparison
            if data == item:
                found = True
                found_node = current_node
            else:
                current_node = current_node.get_next()
        
        return found
    
    def remove(self, item):
        
        current_node = self.head
        previous_node = None
        found = False
        
        while current_node != None and not found:
            
            data = current_node.get_data()
            
            if data == item:
                found = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
            
        #swap
        #item found at head
        if previous_node == None:
            #remove and reassign head
            self.head = current_node.get_next()
        else:
            #remove and reassign the node
            previous_node.set_next(current_node.get_next())
            
        #found at tail
        if current_node == None:
            self.tail = next_node
    
    """
    add to end of the list
    normal looping O(n)
    adding "tail" instance var
    O(n)
    """
    def append(self,item):
        
        #find end of the list
        last_node = None
        
        #check for tail
        if not self.tail == None:
            last_node = self.tail
        else:    
            current_node = self.head
           
            while current_node != None:
                
                next_node = current_node.get_next()
                
                if next_node == None:
                    last_node = next_node
                else:
                    current_node = current_node.get_next()
            
        new_node = Node(item)
        
        last_node.set_next(new_node)
        
        #modify tail
        self.tail = new_node
        
    """
    index(item) returns the position of item in the list. 
    It needs the item and returns the index.
    Assume the item is in the list.
    """
    def index(self, item):
        index = 0
        current_node = self.head
        found = False
       
        
        while current_node != None and not found:

            data = current_node.get_data()
            
            if data == item:
                found = True
            else:
                index = index + 1
                current_node = current_node.get_next()
                
        if found == False:
            return -1
        else:
            return index
        
    """
    if pos == None
    removes and returns the last item in the list
    else:
    removes and returns the item at position pos
    """
    def pop(self, pos=None):
  
        index = 0
        current_node = self.head
        previous_node = None
        found = False
          
        while current_node != None and not found:
            
            if index == pos:
                found = True
            else:
                index = index + 1
                #stop the loop  if the next element is the tail
                # and no position is specified
                # we break so that 
                # we get both the tail
                # and its previous item
                if current_node.get_next() == None and pos == None:
                    break
                else:
                    previous_node = current_node
                    current_node = current_node.get_next()
        
        # pos = None Special case                
        #remove last element
        if pos == None:
            
            #re-confirm last node
            if current_node.get_next() == None:
                
                #remove current_node
                previous_node.set_next(None)    
                
                #set tail
                self.tail = previous_node
                
                return current_node
                
            else:
                return None
        #position specified
        else:
            
            #pos specifed        
            if found == False:
                return None
            else:
                #Position found
                next_node = current_node.get_next()
                
                # position specifed 
                # it is tail - Special case
                if next_node == None:
                    
                    #reassign nodes
                    previous_node.set_next(None)
                    
                    #set tail
                    self.tail = previous_node
                else:
                    
                    #reassign nodes
                    previous_node.set_next(next_node)
                    
                return current_node
        
    def insert(self, pos, item):
        
        index = 0
        current_node = self.head
        previous_node = None
        found = False
          
        while current_node != None and not found:
            if index == pos:
                found = True
            else:
                index = index + 1
                previous_node = current_node
                current_node = current_node.get_next()
    
    
        #newNode
        new_node = Node(item)
    
        #reassign previous nodes next
        # check if pos = 0 ..so no previous node
        if pos == 0:
            #head
            self.head = new_node
        else:    
            previous_node.set_next(new_node)
    
        #set new nodes next
        new_node.set_next(current_node)
          
        return current_node
            
            
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        