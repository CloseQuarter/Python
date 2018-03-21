# -*- coding: utf-8 -*-
"""
Created on Mon Mar 19 22:13:59 2018

@author: sanooj
"""

from DataStructures.OrderedList import OrderedList

mylist = OrderedList()
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist.search(26))
#print(mylist.search(27))

def enumerateList(mylist):
    
    head = mylist.head
    current_node = head
    index = 0
    
    while current_node != None:
        
        print("index = %s data = %s" %(index, current_node.get_data()))
        
        index = index + 1
        current_node = current_node.get_next()
        
    print("list Size: %s " %(mylist.size()))

enumerateList(mylist)

mylist.add(0)

enumerateList(mylist)

mylist.add(1000)

enumerateList(mylist)

mylist.add(32)

enumerateList(mylist)