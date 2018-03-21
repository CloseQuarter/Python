# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 03:40:28 2018

@author: sanooj
"""

#learning numpy
#https://docs.scipy.org/doc/numpy-1.13.0/reference/arrays.indexing.html
import numpy

#Array[startIndex : stopIndex : step]

nArray = [x for x in range(10)]
print(nArray) 
dArray = numpy.arange(10)
#dArray = nArray
print(dArray)#[0 1 2 3 4 5 6 7 8 9]
dArraySlice = dArray[2:7:2] 
print(dArraySlice)#[2 4 6]
print(dArray[0:8]) # [0 1 2 3 4 5 6 7]
print(dArray[:])#[0 1 2 3 4 5 6 7 8 9]
print(dArray[8]) # 8
print(dArray[::]) #[0 1 2 3 4 5 6 7 8 9]
print(dArray[::3]) #[0 3 6 9]
print(dArray[5:7:4]) #[5]
print(dArray[::-4]) #[9 5 1]
print(dArray[::4]) #[0 4 8]
print(dArray[:4]) #[0 1 2 3]
print(dArray[:4:]) #[0 1 2 3]
print(dArray[4::]) #[4 5 6 7 8 9]



