# -*- coding: utf-8 -*-
"""
Created on Sat Jan  6 16:47:56 2018

@author: sanooj
"""

###Tree A New Beginning

class ListC(object):
    def __init__(self):
        self.item = None
        self.next = None
        
    
    
##SEARCH

def search_list(listC,item):
    if None == listC:
        return
    
    if list.item == item:
        return listC
    else:
        return (search_list(listC.next,item))
    

def insert_list(listE,item):
    
    new_list = ListC()
    new_list.item = item
    new_list.next = listE
    
    return new_list
    
listC = None
for element in range(0,4):
    listC = insert_list(listC,element)
    

def predessor_list(listE,item):
    if listE == None or listE.next == None:
        print("has no predecessor")
        return None
    
    if listE.next.item == item:
        return listE
    else:
        return (predessor_list(listE.next,item))
    

def delete_list(listE,item):
    
    #find node
    x_node = search_list(listE,item)
    
    if x_node != None:
        #find predecessor
        p_node = predessor_list(listE,item)
 
        #reorder       
        if p_node != None:
            p_node.next = x_node.next
        else:
            return x_node.next
        
        #free
        x_node = None

def print_list(listC):
    current_list = listC
    while current_list != None:
        print(current_list.item)
        current_list = current_list.next


print_list(listC)

print("predessor_list")
print_list(predessor_list(listC,0))



"""
Binary Search Tree
"""

class BinarySearchTree(object):
    
    def __init__(self):
        self.item   = None  #data
        self.parent = None  #parent
        self.left   = None  #left_child
        self.right  = None  #right_child
        
    def search_tree(self,tree,x):
        
        if tree.item == x:
            return tree
        
        if x < tree.item:
            return tree.search_tree(tree.left,x)
        
        else:
            return tree.search_tree(tree.right,x)
        
    def find_minimum(self,tree):
        
        if tree == None:
            return None
        
        minimum = tree
        
        while minimum.left != None:
            minimum = minimum.left
        
        return minimum
    
    def insert_tree(self,tree,x,parent):
        
        if tree == None or tree.item == None:
            new_tree = BinarySearchTree()
            new_tree.item = x
            new_tree.left = None
            if parent != None:
                parent.right = None
            new_tree.parent = parent
            
            return new_tree
        
        if x < tree.item:
            return self.insert_tree(tree.left,x,tree)
        
        else:
            return self.insert_tree(tree.right,x,tree)



    def traverse_tree(self,tree):
        if tree != None:
            self.traverse_tree(tree.left)
            print(tree.item)
            self.traverse_tree(tree.right)
    
    
binary_tree = BinarySearchTree()
for element in range(0,4):
    binary_tree = binary_tree.insert_tree(binary_tree,element,None)

binary_tree.traverse_tree(binary_tree)





    