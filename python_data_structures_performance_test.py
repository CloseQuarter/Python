# -*- coding: utf-8 -*-
"""
Created on Sun May  7 21:33:26 2017

@author: sanooj
"""


def test1():
        l = []
        for i in range(1000):
            l = l + [i]
            
def test2():
        l = []
        for i in range(1000):
            l.append(i)
            
def test3():
        l = [x for x in range(1000)]
        
def test4():
        l = list(range(1000))
        
import timeit
from timeit import Timer        
def toUseTestClass():
    test = TestClass()
    t1 = Timer("test1()", "from __main__ import test1")
    print("concat ",t1.timeit(number=1000), "milliseconds")
    t2 = Timer("test2()", "from __main__ import test2")
    print("append ",t2.timeit(number=1000), "milliseconds")
    t3 = Timer("test3()", "from __main__ import test3")
    print("comprehension ",t3.timeit(number=1000), "milliseconds")
    t4 = Timer("test4", "from __main__ import test4")
    print("list range ",t4.timeit(number=1000), "milliseconds")

toUseTestClass() 


"""
Parantheses checker
""" 
      