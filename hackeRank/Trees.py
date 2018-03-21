# -*- coding: utf-8 -*-
"""
Created on Tue Jan  9 20:54:49 2018

@author: sanooj
"""

##TREE S

class BinaryTree:
    def __init__(self,rootObj):
        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t


    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
print(r.getRootVal())
print(r.getLeftChild())
r.insertLeft('b')
print(r.getLeftChild())
print(r.getLeftChild().getRootVal())
r.insertRight('c')

"""USING A  STACK TO KEEP TRACK OF THE CURRENT NODE"""
 
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