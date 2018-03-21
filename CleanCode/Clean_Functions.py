# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 21:03:56 2018

@author: sanooj
"""


#INITIAL CODE

class Employee:
    def __init__(self):
        self.type = None
        print("Employee")

def calculatePay(e):
    if e.type == "COMMISSIONED":
        print("COMMISSIONED")
    if e.type == "HOURLY":
        print("HOURLY")
    if e.type == "SALARIED":
        print("SALARIED")
        
        
#cLASS fACtory