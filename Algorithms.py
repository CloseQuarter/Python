# -*- coding: utf-8 -*-
"""
Created on Tue Apr 18 20:57:19 2017

@author: sanooj
"""

def trial():

    print(3//6)
    
    
    print(list(range(10)))
    
    
    david = "David"
    
    print(david.center(10))
    
    print(david.rjust(10))
    
    print(david)
    
    my_name = "David"
    
    print(my_name[:2])
    
    #Tuple
    my_tuple = (2,True,4.9)
    
    print(my_tuple[:1])
    
    #Set
    my_set = {3,6,"cat",4.5}
    
    print(my_set)
    
    for set_elem in my_set:
        print(set_elem)

    print( "len:%i" % (len(my_set)))
    
    #check for membership
    print(3 in my_set)
    
    #dictionary
    capitals = {"iowa":"Desmoines","go":"b"}
    
    for item in capitals:
        #print(key)
        #print(value)
        print(item)
        print(capitals[item])
    
    #list comprehension
    
    sq_list = []
    
    #Without 
    for x in range(1,11):
        sq_list.append(x)
        
    print(sq_list)    
    
    #with
    sq_list = [x * x for x in range(1,11)]

    print(sq_list)

    sq_list = [x*x for x in range(1,11) if x % 2 != 0 ]
    
    print(sq_list)
    
    print([ch.upper() for ch in 'comprehension' if ch in 'aeiou'])
    
    
    
trial()


def classicClasses():
    class Fraction:
            
            def __init__(self,top,bottom):
                self.num =  top
                self.den = bottom
        
            def show(self):
                print(self.num,"/",self.den)
                
            def __str__(self):
                return str(self.num) + "/" + str(self.den)
        
            def __eq__(self,other):
                first_num =  self.num * other.den
                second_num = other.num * self.den
                
                return first_num == second_num
                
    my_fraction = Fraction(3,5)
    print(my_fraction)
    print(my_fraction.show())
    my_fraction.__str__()
    
    
    def gcd(m,n):
        while m %n != 0:
        
            old_m = m
            old_n = n
            
            m = old_n
            n = old_m % old_n
        
        return n
        

classicClasses()
    