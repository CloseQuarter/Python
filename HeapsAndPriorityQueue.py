# -*- coding: utf-8 -*-
"""
Created on Mon Dec 25 16:41:43 2017

@author: sanooj
"""

"""

PRIORITY QUEUE

ENQUEue AND DEQUEue HAPPENS BASED ON PRIORITY

HEAP

Binary heap

O(N log n) .. insertion

2 types

minHeap - min elemnt first

heap order property is as follows:
    In a heap, for every node xx with parent pp,
    the key in "p" is smaller than or equal to the key in "x"

"""

#abstract

class BinaryHeapOperations(object):
    
    def __init__(self):
        pass
    
    def insert(self,k):
        pass
    
    def findMin(self):
        pass
    
    def isEmpty(self):
        pass
    
    def size(self):
        pass
    
    def buildHeap(self,list):
        pass
    
    
class BinaryHeap(BinaryHeapOperations):
    
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    """
    Based on the idea that
    for a parent at "p" left child "x" will be at index 2p
    and right child at 2p + 1
    
    and satisfy heap property
    parent "p" should be <= to child "x"
    """
    def percolateUp(self,i):
        # // - flooring integer division
        while i // 2 > 0: 
            if self.heapList[i] < self.heapList[i // 2]:
                tmp = self.heapList[ i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2
            
    
    def insert(self,k):
        
        #add to end
        self.heapList.append(k)
        
        #increment size
        self.currentSize += 1
        
        #reorder
        self.percolateUp(self.currentSize)
    