# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 21:08:39 2018

@author: sanooj
"""

from DataStructures.UnorderedList import ListADT
from DataStructures.UnorderedList import Node

class OrderedList(ListADT):
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.items = []
        
    def is_empty(self):
        self.items == []
        
    def size(self):
        
        current_node = self.head
        count = 0
        
        while not current_node == None:
            count = count + 1
            current_node = current_node.get_next()
            
        return count
    
    def remove(self,item):
        
        current_node = self.head
        previous_node = None
        index = 0
        found = False
        
        while not current_node == None and not found:
            
            data = current_node.get_data()
            
            if data == item:
                found = True
            else:
                index = index + 1  
                previous_node = current_node
                current_node = current_node.get_next()
        
    
        #reassign     
        # found at head 
        if previous_node == None:
            self.head = current_node
        else:
            next_node = current_node.get_next()
            previous_node.set_next(next_node)
            
             #found at tail
            if next_node == None:
                self.tail = previous_node
             
        return current_node
    
    def search(self, item):
        
        current_node = self.head
        found = False
        #since this is a sorted list
        # we don't need search beyond a value > 
        stop = False
        
        while not current_node == None and not found and not stop:
            
            data = current_node.get_data()
            
            if data == item:
                found = True
            else:
                if data > item:
                    stop = True
                else:    
                    current_node = current_node.get_next()
        
        return found
    
    def add(self, item):
        
        current_node = self.head
        previous_node = None
        stop = False
        
        while not current_node == None and not stop:
            data = current_node.get_data()
            
            # looking to find the node which is 
            # greater than the item
            
            if data > item:
                stop = True
            else:
                previous_node = current_node
                current_node = current_node.get_next()
                
        new_node = Node(item)
        
        #found at head
        if previous_node == None:
            new_node.set_next(self.head)
            self.head = new_node
        else:
            #reassign
            new_node.set_next(current_node)
            previous_node.set_next(new_node)
        
                
    