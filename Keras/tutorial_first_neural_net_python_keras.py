# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 03:22:51 2018

@author: sanooj
"""

##BACKEMD = tensorflow
##TEST - from keras import backend; print(backend._BACKEND)
#Dataset - 

#C:\Users\sanooj\OneDrive\Books_Not_Sorted_yet\Algorithms\Python\Keras
#pima-indians-diabetes.data.csv

#http://archive.ics.uci.edu/ml/datasets/Pima+Indians+Diabetes

#TUTORIAL SITE
#https://machinelearningmastery.com/tutorial-first-neural-network-python-keras/
#https://www.dotnetperls.com/slice-python

from keras.models import Sequential
from keras.layers import Dense
import numpy

#fix random seed for reproducibility
numpy.random.seed(7)

DATASET = "pima-indians-diabetes.data.csv"

#load pima indians dataset
dataset = numpy.loadtxt(DATASET,delimiter=",")

print(type(dataset))
print(dataset)


#split into input X and output Y variables
X = dataset[:,0:8]
"""
2D Array

first Array -> all elemnts
second Array -> 0 to 8 indexes

"""
print("X = %s" %(X))

Y = dataset[:,8]
"""
2D Array

first Array -> all elemnts
second Array -> only 8th index

"""
print("Y = %s" %(Y))
