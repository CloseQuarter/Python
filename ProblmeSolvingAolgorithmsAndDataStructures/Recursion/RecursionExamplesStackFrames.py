# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 03:51:28 2018

@author: sanooj
"""

import sys
import os

#print(os.path.dirname(__file__))

from os.path import join, getsize
for root, dirs, files in os.walk(os.path.dirname(__file__)):
    print(root)

path = (
        "C:\\Users\\sanooj\\OneDrive\\"
        "Books_Not_Sorted_yet\\Algorithms\\"
        "Python\\ProblmeSolvingAolgorithmsAndDataStructures"
        )

sys.path.append(
        path
        )

from BasicDataStructures.DataStructures.Stack import Stack


def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    if n < base:
        return convert_string[n]
    else:
        return to_str(n / base, base) + convert_string[n % base]

#print(to_str(1453, 16))


r_stack = Stack()

def to_str_using_stack(n, base):
    
    convert_string = \
    "0123456789ABCDEF"
    
    while n> 0:
        print("stack %s" %(r_stack.items))
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[ n % base])
            
        n = n // base
        
    res = ""
    
    print("stack %s" %(r_stack.items))
    
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res

#print(to_str_using_stack(1453, 16))
print(to_str_using_stack(10, 2))
        
"""
Turtle Graphics
"""    

import turtle

my_turtle = turtle.Turtle()
my_win = turtle.Screen()

def draw_spiral(my_turtle, line_len):
    
    if line_len > 0:
        
        my_turtle.forward(line_len)
        my_turtle.right(90)
        
        draw_spiral(my_turtle, line_len - 5)
        
#draw_spiral(my_turtle, 100)
#my_win.exitonclick()

#def tree(branch_len, t):
#    
#    if branch_len > 5:
#        t.forward(branch_len)
#        t.right(20)
#        tree(branch_len - 15, t)
#        t.left(40)
#        tree(branch_len - 15, t)
#        t.right(20)
#        t.backward(branch_len)
#        
#def main():
#    t = turtle.Turtle()
#    my_win = turtle.Screen()
#    t.left(90)
#    t.up()
#    t.backward(100)
#    t.down()
#    t.color("green")
#    tree(75, t)
#    my_win.exitonclick()
#main()


def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0], points[1][1])
    my_turtle.goto(points[2][0], points[2][1])
    my_turtle.goto(points[0][0], points[0][1])
    my_turtle.end_fill()
    
draw_triangle([0,100],'red',my_turtle)
            