# -*- coding: utf-8 -*-
"""
Created on Sat Dec 23 12:31:37 2017

@author: sanooj
"""

#Creating a tree with an array
"""
Tre has left and right parts
"""
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
        
#Abstract Class
class BinaryTreeOperations(object):
    def __init__(self,root):
        self.key  = root
        self.leftChild = None
        self.rightChild = None
        #added for binary search tree
        self.parent = None
    
    #getLeftTree
    def getLeftChild(self):
        return None
    
    #getRightTree
    def getRightChild(self):
        return None
    
    #getRoot
    def getRoot(self):
        return None
    
    #setRoot
    def setRoot(self,key):
        pass
    
    #insertRight
    def insertRight(self,value):
        pass    
    
    #insertLeft
    def insertLeft(self,value):
        pass

class BinaryTree(BinaryTreeOperations):
    
    def __init__(self,root):
       super().__init__(root)
       
    #getLeftTree
    def getLeftChild(self):
        return self.leftChild
    
    #getRightTree
    def getRightChild(self):
        return self.rightChild
    
    #getRoot
    def getRoot(self):
        return self.key
    
    #setRoot
    def setRoot(self,key):
        self.key = key
       
    #insertRight
    def insertRight(self,value):
        
        #make a node
        node = BinaryTree(value)
        
        #check if right side of tree exists
        rightChild = self.getRightChild()
        
        if rightChild != None:
            #if left side exists
            currentRightTree = rightChild
            
            #reorder
            node.rightChild = currentRightTree
            
            #assign new node as right tree
            self.rightChild = node
        else:
            #else
            
            #add to right
            self.rightChild = node
    
    #insertLeft        
    def insertLeft(self,value):
        
        #make a new node
        node = BinaryTree(value)
        
        #check if left side of tree exists
        leftChild = self.getLeftChild()
        
        if leftChild != None:
            #if left side exists
            currentLeftTree = leftChild
            
            #reorder
            node.leftChild = currentLeftTree
            
            #assign new node as left tree
            self.leftChild = node
        else:
            #else
            
            #add to left
            self.leftChild = node
            
            
"""
""""""MAKING THIS TREE"""
""""
           1                 0
         /   \
        2     3         1         2
       /\     /\      3    4   5     6
      4  5   6  7
"""


def isABinaryTreeFilled(tree):
    if tree.leftChild != None and tree.rightChild != None:
        return True
    else:
        return False

array = [1,2,3,4,5,6,7]
print("Binary tree With Node")
def makeABinaryTree():
    import math
    tree = BinaryTree(array[0])
    """
     x
  b       = a         

then

  log a = x
     b
    """
    maxNodeCount = math.ceil(math.log(len(array),2))
    print("max %s"%(maxNodeCount))
    
    level = 1
    
    currentNode = tree
    
    parentNode = Stack()
    parentNode.push(tree)   ~   
    
    for element in array[1:len(array)]:
        
        ## both left and right empty
        if currentNode.leftChild == None:
            print("create a new left node")
            node = BinaryTree(element)
            currentNode.leftChild = node
            #currentNode = node
            level += 1
            parentNode.push(tree)
        
        #left filled but right empty
        elif currentNode.rightChild == None and currentNode.leftChild != None:
            print("create a new right node")
            node = BinaryTree(element)
            #fill right
            currentNode.rightChild = node
            #save left
            currentNode = currentNode.leftChild
            #move to parent
            parentNode .pop()
                    
    return tree

pj = makeABinaryTree()
def preorder(tree):
    if tree:
        print(tree.getRoot())
        print("getLeftChild")
        preorder(tree.getLeftChild())
        print("getRighChild")
        preorder(tree.getRightChild())
    
preorder(pj)

print("in order")
def inorder(tree): 
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRoot())
        inorder(tree.getRightChild())
        
        
inorder(pj)


#make with recursion
def insert(tree = None,data):
    
    child = BinaryTree(data)
    child.parent = tree
    
    if tree == None:
        return child
    
    if tree.leftChild == None:
        tree.leftChild = child
    else if tree.rightChild == None:
        tree.rightChild = child
    
    return tree

def isTreeFull(tree):
    
    #Nil check
    if tree == None: 
        return False
    
    if tree.leftChild and tree.RightChild:
        return True
    else:
        return False
    

def make(array = [1,2,3,4,5,6,7]):
    tree = BinaryTree(array[0])
    for element in array[1:len(array)]:
        if tree
        
     
            
        
        
    
