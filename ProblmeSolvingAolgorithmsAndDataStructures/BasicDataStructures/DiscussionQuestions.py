# -*- coding: utf-8 -*-
"""
Created on Wed Mar 21 03:55:39 2018

@author: sanooj
"""

"""
1. Convert the following values to binary using
 “divide by 2.” Show the stack of remainders.
• 17
• 45
• 96
"""

from DataStructures.Stack import Stack
from enum import Enum

class Base(Enum):
    BINARY = 2
    HEX    = 16
    OCTA   = 8

"""
"""
def dq_divide_by_base(base , element):
    
    """
    Summary
    -------------
    Convert the give number (element) to 
    a number in the specified Base (base)
    if none specified, Binary is assumed
    
    Logic
    -----
    Perform divide_by_2 algorithm extended to use 
    for all bases

    store reminders in a Stack
    
    enumerate the Stack
    
    use each element in the stack as an index to a digit set
    corresponding to each base
    
    convert all elemnts in te stack to the corresponding elements in the 
    digit set 
    
    Parameters
    ----------
    arg1 : base
        base. 
        Member of "Base" enum class
        specifies what base needs to be used
        BINARY.HEX.OCT are supported
    arg2 : element
        element. 
        Memeber of "int" class
        number to be converted

    Returns
    -------
    str
        number in desired base

    """
    
    binary_digit_set = [0,1,2,3,4,5,6,7,8,9]
    hex_digit_set = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    oct_digit_set = [0,1,2,3,4,5,6,7]
    
    divisor = 0
    
    #find the appropriate divisor to perform divide_by_base algorithm
    if base == Base.BINARY:
        divisor = Base.BINARY.value
    
    if base == Base.HEX:
        divisor = Base.HEX.value
        
    if base == Base.OCTA:
        divisor = Base.OCTA.value
    
    
    reminder_stack = Stack()
    reminder = 0
    quotient = element
    
    #divide_by_base algorithm
    while quotient > 0:
        
        reminder = quotient % divisor
        quotient = quotient // divisor
        
        #push reminder to stack
        reminder_stack.push(reminder)
        
    print(reminder_stack.items)
    
    number_string  = ""
    
    #convert number to string
    #substitude characters from digit_sets
    while not reminder_stack.is_empty():
        
        digit = ""
        final_reminder = reminder_stack.pop()
        
        if base == Base.BINARY:
            digit = str(binary_digit_set[final_reminder])
            
        if base == Base.HEX:
            digit = hex_digit_set[final_reminder]
            
            if digit is str:
                digit = str(digit)
        
        if base == Base.OCTA:
            digit = str(oct_digit_set[final_reminder])
            
        
        number_string = number_string + digit 
    
    return number_string

print("test_dq_divide_by_base")
def test_dq_divide_by_base():
    print(dq_divide_by_base(Base.BINARY,3))
    print(dq_divide_by_base(Base.HEX,11)) 
    print(dq_divide_by_base(Base.HEX,2748)) #ABC
    print(dq_divide_by_base(Base.OCTA,2748)) #5274
    print("17 %s" %(dq_divide_by_base(Base.BINARY,17)))
    print("45 %s" %(dq_divide_by_base(Base.BINARY,45)))
    print("96 %s" %(dq_divide_by_base(Base.BINARY,96)))

test_dq_divide_by_base()

########################################################################################
#########################################################################################



"""
2. Convert the following infix expressions to prefix (use full parentheses):
     ( A + B * ( C + D ) * ( E + F ))
       A + ((B + C) * ( D + E ))
       A * B * C * D + E + F
"""

def dq_infix_to_postfix(infix_expr):
    
    #precedence table
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    
    alaphabet_tokens = \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    numeral_tokens = \
    "0123456789"
    
    #stack to hold operators
    op_stack = Stack()
    
    #list to hold operands
    #and final result
    postfix_list = []
    
    #split the expression
    tokens_list = \
    infix_expr.split()
    
    #evaluate the expression
    for token in tokens_list:
        
        if token in alaphabet_tokens or \
        token in numeral_tokens:
        
            postfix_list.append(token)
            
        if token == "(":
            
            op_stack.push()
            
        if token in "*+/-":
            
            op_stack.push(token)
                
        if token is ")":
            
            op = ""
            
            while not op is "(":
                
                postfix_list.append(op_stack.pop())
                
                







