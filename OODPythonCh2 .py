# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 00:21:31 2017

@author: sanooj
"""

class MyFirstClass:
    pass

a = MyFirstClass()
b = MyFirstClass()

print(a)
print(b)

class Point:
    def reset(self):
        self.x = 0
        self.y = 0
    pass

p1 = Point()
p2 = Point()

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)


p = Point()
#p.reset()
#p.x = 9
#p.y = 10
#print(p.x,p.y)
Point.reset(p)
print(p.x,p.y)

import math

class PointA(Point):
    def move(self,x,y):
        self.x = x
        self.y = y
        
    def reset(self):
        self.move(1,0)
        
    def calculate_distance(self,other_point):
        return math.sqrt((self.x - other_point.x) **2 +
                         (self.y - other_point.y) **2
                         )


pointb = PointA()
pointc = PointA()

pointb.reset()
pointb.move(5,0)

print(pointb)
print(pointb.x,pointb.y)

pointc.reset()

print(pointc)
print(pointc.x,pointc.y)

print(pointb.calculate_distance(pointc))


#Bubble Sort
intArray = [2,5,4]
print(intArray)
print(len(intArray))
print(type(len(intArray)))

def bubbleSortThis(intArray):
    for i in range(0,len(intArray)):
        for j in range(0,len(intArray)):
            if intArray[i] < intArray[j]:
                tmp = intArray[j]
                intArray[j] = intArray[i]
                intArray[i] = tmp
    print(intArray)

bubbleSortThis(intArray)

print([67].__add__([55,88]))



import django

print("django version" + " " + django.get_version())