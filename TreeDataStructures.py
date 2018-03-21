# -*- coding: utf-8 -*-
"""
Created on Fri Dec 15 19:41:18 2017

@author: sanooj
"""

"""



Tree data Structures

1. hierarchical
        general things on top
        specific things at bottom
        
        all children of one node are independent of children
        of other nodes
        
        each leaf node is unique
        
        move portion of tree (subtree) to a different poistion
        without affecting lower levels
        
Node - Member of a tree -- also called "key"
Edge - connection between 2 or more nodes
        every node has one incoming edge 
            - except "root" node"
root - node with no icoming connection

path - list of nodes connected by edges

children 
        - nodes that share same incoming edge
        
parent
        the node form which the incoming edge originates
    
sibling
        children of the same parent

subtree
        parent and all its descendants
        
leaf node
        node with no children
        
Level
        number of edges on the path from root node
        
height 
        max level of any node in the tree
"""

""""
           a 
        |     \
        b      c
        | \    |
        d  e    f
"""

"""
Simplified Tree
Binary tree with list
1. each node is a lits of 3 members,
     including itself
2. root node is not a list
3. children are lists
4 eg ["root" , [children], [children]]
constructs a list with a root node and two empty sublists for the children. 
"""

myTree = [ "a", #root
          ["b", #left subtree
           ["d",[],[] 
           ] ,
           ["e",[],[] 
           ] 
           ] ,
          ["c", #right subtree
           ["f", [] , []
           ],
           [] 
           ]
        ]

#root
print(myTree[0]) 

#left subtree
print(myTree[1])

#right subtree
print(myTree[2])


def BinaryTree(root,left = [], right = []):
    return [root,left,right]

def insertLeft(root, new_branch):
    t = root.pop(1)
    if len(t) > 1:
        #root.insert(1,[new_branch,t,[]])
        root.insert(1,BinaryTree(new_branch,t,[]))
    else:
        #root.insert(1,[new_branch,[],[]])
        root.insert(1,BinaryTree(new_branch))
    
    return root

def insertRight(root, new_branch):
    t = root.pop(2)
    if len(t) > 1:
        #root.insert(2,[new_branch,[],t])
        root.insert(2,BinaryTree(new_branch,[],t))
    else:
        #root.insert(2,[new_branch,[],[]])
        root.insert(2,BinaryTree(new_branch,[],[]))
    
    return root

def getRootVal(root):
    return root[0]

def setRootVal(root,new_value):
    root[0] = new_value

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]



print("myTree")
#insertRight(myTree[2],"g")

#root
#print(myTree[0]) 

#left subtree
#print(myTree[1])

#right subtree
#print(myTree[2])

#r = BinaryTree(3)
#print(r)
#insertRight(r,3.5)
#print(r)
#insertLeft(r,4)
#print(r)
##insertLeft(r,5)
##print(r)
##insertRight(r,6)
##print(r)
##insertRight(r,7)
##print(r)
#l = getLeftChild(r)
##print(r)
#print(l)
##
#setRootVal(l,9)
#print(r)
##insertLeft(l,11)
##print(r)
#print(getRightChild(getRightChild(r)))

"""MAKING THIS TREE"""
""""
           a 
        |     \
        b      c
         \    / \
          d  e  f
"""
def making_a_tree():
    #adding root
    root = BinaryTree("a")
    print(root)
    #adding right child
    insertRight(root,"c")
    print(root)
    #adding left child
    insertLeft(root,"b")
    print(root)
    """insert right child to leftchild of root"""
    #get right child of root
    left_child = getLeftChild(root)
    print("left_child %s" %(left_child))
    #insert right child
    insertRight(left_child,"d")
    print(root)
    """insert left child to righchild of root"""
    #getrightchild of root
    right_child = getRightChild(root)
    print("right_child %s" %(right_child))
    #insert left child
    insertLeft(right_child,"e")
    print(root)
    #insert right child
    insertRight(right_child,"f")
    print(root)
making_a_tree()


class BinaryTreeC:
    
    def __init__(self,root,left = [],right = []):
        self.root = BinaryTreeC.make(root)
    
    def make(root,left = [],right =[]):
        return [root,left,right]
    
    def insert_left(self,new_branch):
        tmp_root = self.root.pop(1)
        if len(tmp_root) > 1:
            tree = BinaryTreeC.make(new_branch,tmp_root,[])
            self.root.insert(1,tree)
        else:
            tree = BinaryTreeC.make(new_branch,[],[])
            self.root.insert(1, tree)
    
    def insert_right(self,new_branch):
        tmp_root = self.root.pop(2)
        if len(tmp_root) > 1:
            tree = BinaryTreeC.make(new_branch,[],tmp_root)
            self.root.insert(2, tree)
        else:
            tree = BinaryTreeC.make(new_branch,[],[])
            self.root.insert(2, tree)

    def get_root_val(self,root):
        return root.root[0]

    def setRootVal(self,root,new_value):
        root.root[0] = new_value

    def getLeftChild(self,root):
        return root.root[1]

    def getRightChild(self,root):
        return root.root[2]


binary_tree = BinaryTreeC(1)
print("binary_tree")
print(binary_tree.root)
binary_tree.insert_left(2)
print(binary_tree.root)
binary_tree.insert_right(3)
print(binary_tree.root)
"""insert right child to leftchild of root"""
#get left child of root
left_child = binary_tree.getLeftChild(binary_tree)
print("left_child %s" %(left_child))
#get right child of root
right_child = binary_tree.getRightChild(binary_tree)
print("right_child %s" %(right_child))
#insert_left of left child
left_child = binary_tree.getLeftChild(binary_tree)
binary_tree.insert_left(4)
print(binary_tree.root)
#insert_right of right tree
right_child = binary_tree.getRightChild(binary_tree)
binary_tree.insert_right(5)
print(binary_tree.root)


"""TREE WITH NODES"""
class BinaryTreeN:
    def __init__(self,root_obj = ""):
        self.key = root_obj
        self.left_child = None
        self.right_child = None
        
    def insert_right(self,new_node):
        tree = BinaryTreeN(new_node)
        if self.right_child == None:
            self.right_child = tree
        else:
            tree.right_child = self.right_child
            self.right_child = tree
            
    def insert_left(self,new_node):
        tree = BinaryTreeN(new_node)
        if self.left_child == None: #no left child
            tree = BinaryTreeN(new_node)
            self.left_child = tree
        else:
            #insert new node before ciurrent node
            tree.left_child = self.left_child
            self.left_child = tree
    
    def getRightChild(self):
        return self.right_child
    
    def getLeftChild(self):
        return self.left_child
    
    ##replace rootval
    def setRootVal(self,new_root):
        self.key = new_root
        
    def getRootVal(self):
        return self.key


"""MAKING THIS TREE"""
""""
           a 
         /   \
        b      c
         \    / \
          d  e  f
"""
print("Binary tree With Node")
def make_tree_():
    r = BinaryTreeN('a')
    print(r.getRootVal())
    print(r.getLeftChild())
    #left child
    r.insert_left('b')
    print(r.getLeftChild().getRootVal())
    #right child
    r.insert_right('c')
    print(r.getRightChild().getRootVal())
    #insert at left child's right
    left_child = r.getLeftChild()
    left_child.insert_right("d")
    print(r.getLeftChild().getRightChild().getRootVal())
     #insert at right child's left and right
    right_child = r.getRightChild()
    right_child.insert_left("e")
    right_child.insert_right("f")
    print(r.getRightChild().getLeftChild().getRootVal() == "e")
    print(r.getRightChild().getRightChild().getRootVal() == "f")
    
make_tree_()

"""PARSE TREES"""

"""
Using the information from above we can define 
four rules as follows:

1.If the current token is a '(', 
    a. add a new node as the left child of the current node, and 
    b. descend to the left child.
2.If the current token is in the list ['+','-','/','*'],
    a. set the root value of the current node 
        to the operator represented by the current token.
    b. Add a new node as the right child of the current node and
    c. descend to the right child.
3.If the current token is a number,
    a. set the root value of the current node to the number and
    b. return to the parent.
4.If the current token is a ')',
    a.go to the parent of the current node.
 
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
        

def buildParseTree(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTreeN("")
    #push current node
    pStack.push(eTree)
    #hold currentTree
    currentTree = eTree
    
    for i in fplist:
        if i == "(":
            #rule 1 add a new node to left
            currentTree.insert_left("")
            #save parent
            pStack.push(currentTree)
            #navigate to that node
            currentTree = currentTree.getLeftChild()
        elif i  in ['+','-','*','/']:
            #rule 2
            # add the operatorValue to root
            currentTree.setRootVal(i)
            #insert right
            currentTree.insert_right("")
            #save parent
            pStack.push(currentTree)
            #navigate to current
            currentTree = currentTree.getRightChild()
            
        elif i == ")":
            #rule 3
            # go to parent of current node
            #pop to parent
            currentTree = pStack.pop()
        elif i not in ['(','+','-','*','/',')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            
            except ValueError:
                raise ValueError(
                        "token '{}' is not a valid integer".format(i)
                        )
            
    return eTree
 
pt = buildParseTree("( ( 10 + 5 ) * 3 )")
print(pt.getRootVal())
print(pt.getLeftChild().getRootVal())
print(pt.getRightChild().getRootVal())
print(pt.getLeftChild().getLeftChild().getRootVal())  
print(pt.getLeftChild().getRightChild().getRootVal())  

import operator 

print("Binary tree With Node")
def evaluate(parseTree):
    operators = {
            "+" : operator.add, #holds the function
            "-" : operator.sub,
            "*" : operator.mul,
            "/" : operator.truediv
            }
    
    def print_(specifier,val):
        if not val == None:
            print(specifier %(val.getRootVal()))
        else: 
            print(specifier %(val))
        
    leftC = parseTree.getLeftChild()
    print_("leftC %s", leftC)
    #print_(leftC)
    
    rightC = parseTree.getRightChild()
    print_("rightC %s" , rightC)
    #print_(rightC)
    
    
    if leftC and rightC:
        fn = operators[parseTree.getRootVal()]
        print("fn %s" %(fn))
        print("leftCEval start")
        leftCEval = evaluate(leftC)
        print("leftCEval %s" %(leftCEval))
        print("rightCEval start")
        rightCEval = evaluate(rightC)
        print("rightCEval %s" %(rightCEval))
        rtn =  fn(leftCEval,rightCEval)
        print("rtn %s" %(rtn))
        return rtn
    else:
        rtv =  parseTree.getRootVal()
        print("rtv %s" %(rtv))
        return rtv

print(evaluate(pt))


"""
TREE TRAVERSAL
"""

"""
PREORDER

1. we visit the root node first, 
2. then recursively do a preorder traversal of the left subtree,
3. followed by a recursive preorder traversal of the right subtree.
"""



"""
INORDER

1.we recursively do an inorder traversal on the left subtree,
 visit the root node, 
 and finally do a recursive inorder traversal of the right subtree.

"""


"""
POSTORDER

1. we recursively do a postorder traversal of the left subtree
2. and the right subtree 
3. followed by a visit to the root node.

"""

print("preorder")
""""
           * 
         /   \
        +      3
       /  \    
      10   5  
"""
#"( ( 10 + 5 ) * 3 )"
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        print("getLeftChild")
        preorder(tree.getLeftChild())
        print("getRighChild")
        preorder(tree.getRightChild())
    
preorder(pt)

def buildParseTreeForPreOrdering(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTreePreOrdering("")
    #push current node
    pStack.push(eTree)
    #hold currentTree
    currentTree = eTree
    
    for i in fplist:
        if i == "(":
            #rule 1 add a new node to left
            currentTree.insert_left("")
            #save parent
            pStack.push(currentTree)
            #navigate to that node
            currentTree = currentTree.getLeftChild()
        elif i  in ['+','-','*','/']:
            #rule 2
            # add the operatorValue to root
            currentTree.setRootVal(i)
            #insert right
            currentTree.insert_right("")
            #save parent
            pStack.push(currentTree)
            #navigate to current
            currentTree = currentTree.getRightChild()
            
        elif i == ")":
            #rule 3
            # go to parent of current node
            #pop to parent
            currentTree = pStack.pop()
        elif i not in ['(','+','-','*','/',')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            
            except ValueError:
                raise ValueError(
                        "token '{}' is not a valid integer".format(i)
                        )
            
    return eTree

""""
           * 
         /   \
        +      3
       /  \    
      10   5  
"""
#"( ( 10 + 5 ) * 3 )"
#Preorder wwith errror checking
print("Preorder wwith errror checking")
class BinaryTreePreOrdering(BinaryTreeN):
    
    def insert_right(self,new_node):
        tree = BinaryTreePreOrdering(new_node)
        if self.right_child == None:
            self.right_child = tree
        else:
            tree.right_child = self.right_child
            self.right_child = tree
            
    def insert_left(self,new_node):
        tree = BinaryTreePreOrdering(new_node)
        if self.left_child == None: #no left child
            tree = BinaryTreePreOrdering(new_node)
            self.left_child = tree
        else:
            #insert new node before ciurrent node
            tree.left_child = self.left_child
            self.left_child = tree
            
    def preorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.preorder()
        if self.right_child:
            self.right_child.preorder()
        
pt_ = buildParseTreeForPreOrdering("( ( 10 + 5 ) * 3 )")
pt_.preorder()
#print(pt_.getRootVal())
#print(pt_.getLeftChild().getRootVal())
#print(pt_.getRightChild().getRootVal())
#print(pt_.getLeftChild().getLeftChild().getRootVal())  
#print(pt_.getLeftChild().getRightChild().getRootVal())  

""""
           * 
         /   \
        +      3
       /  \    
      10   5  
"""
#"( ( 10 + 5 ) * 3 )"
#postorder wwith errror checking
print("postorder wwith errror checking")
#postorder
def buildParseTreeForPostOrdering(fpexp):
    fplist = fpexp.split()
    pStack = Stack()
    eTree = BinaryTreePostOrdering("")
    #push current node
    pStack.push(eTree)
    #hold currentTree
    currentTree = eTree
    
    for i in fplist:
        if i == "(":
            #rule 1 add a new node to left
            currentTree.insert_left("")
            #save parent
            pStack.push(currentTree)
            #navigate to that node
            currentTree = currentTree.getLeftChild()
        elif i  in ['+','-','*','/']:
            #rule 2
            # add the operatorValue to root
            currentTree.setRootVal(i)
            #insert right
            currentTree.insert_right("")
            #save parent
            pStack.push(currentTree)
            #navigate to current
            currentTree = currentTree.getRightChild()
            
        elif i == ")":
            #rule 3
            # go to parent of current node
            #pop to parent
            currentTree = pStack.pop()
        elif i not in ['(','+','-','*','/',')']:
            try:
                currentTree.setRootVal(int(i))
                parent = pStack.pop()
                currentTree = parent
            
            except ValueError:
                raise ValueError(
                        "token '{}' is not a valid integer".format(i)
                        )
            
    return eTree
class BinaryTreePostOrdering(BinaryTreeN):
    
    def insert_right(self,new_node):
        tree = BinaryTreePostOrdering(new_node)
        if self.right_child == None:
            self.right_child = tree
        else:
            tree.right_child = self.right_child
            self.right_child = tree
            
    def insert_left(self,new_node):
        tree = BinaryTreePostOrdering(new_node)
        if self.left_child == None: #no left child
            tree = BinaryTreePostOrdering(new_node)
            self.left_child = tree
        else:
            #insert new node before ciurrent node
            tree.left_child = self.left_child
            self.left_child = tree
            
    def postorder(self):
        print(self.key)
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()

pt__ = buildParseTreeForPostOrdering("( ( 10 + 5 ) * 3 )")
#pt__.postorder()
#print(pt__.getRootVal())
#print(pt__.getLeftChild().getRootVal())
#print(pt__.getRightChild().getRootVal())
#print(pt__.getLeftChild().getLeftChild().getRootVal())  
#print(pt__.getLeftChild().getRightChild().getRootVal())
  
def postorder(tree): 
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRightChild())
        print(tree.getRootVal())
        
postorder(pt__)

""""
           * 
         /   \
        +      3
       /  \    
      10   5  
"""
#"( ( 10 + 5 ) * 3 )"
print("in order")
def inorder(tree): 
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())
        
        
inorder(pt__)

print("printexp")
def printexp(tree):
  sVal = ""
  print(sVal)
  if tree:
      sVal = '(' + printexp(tree.getLeftChild())
      sVal = sVal + str(tree.getRootVal())
      sVal = sVal + printexp(tree.getRightChild())+')'
  return sVal

printexp(pt__)