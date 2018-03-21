# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 21:00:49 2018

@author: sanooj
"""

from DataStructures.UnorderedList import UnOrderedList

mylist = UnOrderedList()
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
        
mylist.remove(26)

enumerateList(mylist)

#test index
def testIndex(elem):
    print("index of: %s = %s" %(elem,mylist.index(elem)))
    
testIndex(31)
testIndex(77)
testIndex(100)

enumerateList(mylist)

#test Append
def testAppend(elem):
    mylist.append(elem)
    print("index of: %s = %s" %(elem,mylist.index(elem)))
    
testAppend(99)
testAppend(98)

enumerateList(mylist)

#test pop
print("test pop")
def testPop(pos=None):
    popped_item = mylist.pop(pos)
    if not popped_item == None:
        print(
                "popped off %s = %s" 
                %(pos,popped_item.get_data())
                )
    else:
        print("NotFound")
    
#testPop()

#enumerateList(mylist)

testPop(5)
enumerateList(mylist)


print("test insert")
#test insert
def testInsert(item,pos=0):
    mylist.insert(pos,item)

#testInsert(101)

enumerateList(mylist)

testInsert(102,5)

enumerateList(mylist)