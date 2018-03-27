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
    """
    #1 match alphabet or numeral tokes and add them to  
    """
    #enumerate the expression
    for token in tokens_list:
        
        #look for a matching alphabet or numeral token
        if token in alaphabet_tokens or \
        token in numeral_tokens :
            
            #if matches add it to postfix_list
            postfix_list.append(token)
            
        #look for matching "(" 
        #push it to operand stack
        elif token == "(":
            op_stack.push(token)
        
        #look for closing braces )
        elif token == ")":
            """
            #1 closing - means end of scope
            #2 so we need to pop the stack
            #3 utill we get the corresponding open "("
            #4 add all the appended operators to the output
            """
            top_token = op_stack.pop()
            while top_token != "(":
                postfix_list.append(top_token)
                top_token = op_stack.pop()
        
        #for all other symbols
        else:
        
            #ie. for +,*,-./
            # compare with all ops in the op_stack
            # find out if there is any operator with higher precedence
            # if yes add all of them to output
            # push to op_stack
                    
            while not op_stack.is_empty() and \
            prec[op_stack.peek()] >= prec[token] :
                
                #pop it
                oper = op_stack.pop()
                
                #add to output
                postfix_list.append(oper)
            
            #if op_stack is empty    
            #push the operator to op_stack
            op_stack.push(token)    
            
       #expression enumration complete
   
    #loop through opstack
    while not op_stack.is_empty():
        #add them to output
        postfix_list.append(op_stack.pop())
    
    #join the string
    return " ".join(postfix_list)

#print(dq_infix_to_postfix("( ( A + B ) * C )"))
#print(dq_infix_to_postfix("( A * ( B + C ) )"))


def dq_infix_to_prefix(infix_expr):
    
    #precedence table
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    
    alaphabet_tokens = \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    numeral_tokens = \
    "0123456789"
    
    #stack to hold operators
    op_stack = Stack()
    
    #list to hold operands
    #and final result
    prefix_list = []
    
    #split the expression
    tokens_list = \
    infix_expr.split()
    
    #print("tokens_list %s" %(tokens_list))
    
    # evaluate the expression
    # we start evaluating left to right
    # 1. reverse the list
    tokens_list_reversed = \
    tokens_list[::-1] 
    
    #print("tokens_list_reversed %s" %(tokens_list_reversed))
    #print("tokens_list %s" %(tokens_list))
    
    
    #expression enumration begin
    for token in tokens_list_reversed:
        #2. case ")"
        # since we start from the end of the expression
        # we consider "(" to be end of the grouping
        if token is ")":
            op_stack.push(token)
            
        #3.case operand 
        elif token in alaphabet_tokens or \
        token in numeral_tokens:
            prefix_list.append(token)
            
        #4. case "("
        elif token is "(":
            # marks the end of expression or
            # closing of  a grouping ()
            # move all operators till "(" to output
            
            
            top_operator = \
            op_stack.pop()
            
            while not  top_operator is ")":
                prefix_list.append(top_operator)
                top_operator = \
                op_stack.pop()
                
        else:
            
            #ie. for +,*,-./
            # compare with all ops in the op_stack
            # find out if there is any operator with higher precedence
            # if yes add all of them to output
            # push to op_stack
                    
            while not op_stack.is_empty() and \
            prec[op_stack.peek()] >= prec[token]:
                
                #move them to output
                operator = \
                op_stack.pop()
                
                prefix_list.append(operator)
                
            #if op_stack is empty    
            #push the operator to op_stack
            op_stack.push(token)    
            
       #expression enumration complete
       
    #move the remaining items
    while not op_stack.is_empty():
           
       operator = \
       op_stack.pop()
            
       prefix_list.append(operator)
           
    #join the string
    return " ".join(prefix_list[::-1])
    
def dq_test_infix_to_prefix_or_postfix():    
    print(dq_infix_to_prefix("( A + B )"))
    print(dq_infix_to_prefix("( A * ( B + C ) )"))
    print(dq_infix_to_prefix("A * B + C"))
    print(dq_infix_to_prefix("( ( A * B ) + C )"))
    print(dq_infix_to_postfix("( A * ( B + C ) )"))
    print(dq_infix_to_postfix("( ( A * B ) + C )"))
    print(dq_infix_to_postfix("A * B + C"))

exp = "( A + B ) * ( C + D ) * ( E + F )"
print(
       "%s ==> \n %s" 
      %(exp, dq_infix_to_postfix(exp))
      )
print(
       "%s ==> \n %s" 
      %(exp, dq_infix_to_prefix(exp))
      )

"""
Evaluate the following postfix expressions.
 Show the stack as each operand and operator
is processed.

• 23 * 4+
• 12 + 3 + 4 + 5+
• 12345 * + * +

"""
def dq_evaluate_postfix(postfix_expr):

    """
    1. add numbesr to stack
    2. whne you reach an operator 
            pop the stack twice
    3 perform the math of the opeartor
    """    
    
    print(postfix_expr)
    
    op_stack = Stack()
    
    numeral_tokens = \
    "0123456789"
    
    operator_tokens = \
    "+-*/"
        
    import operator
    
    operator_to_fn_map = \
    {
     "+" : operator.add,
     "*" : operator.mul,
     "-" : operator.sub,
     "/" : operator.__truediv__,
    }
    
    #start parsing
    for token in postfix_expr:
        
        print("Stack -> %s" %(op_stack.items))
        
        #case operand
        if token in numeral_tokens:
            op_stack.push(token)
            
        #case operator
        elif token in operator_tokens:
            
            second_operand = \
            op_stack.pop()
            
            first_operand = \
            op_stack.pop()
            
            #perform math
            operator_fn = \
            operator_to_fn_map[token]
            
            result = \
            operator_fn(
                    int(first_operand),
                    int(second_operand)
                    )
            #push result to stack
            op_stack.push(result)
            
    return op_stack.pop()
    
    
print(dq_evaluate_postfix("23 * 4+"))
print(dq_evaluate_postfix("12 + 3 + 4 + 5+"))
print(dq_evaluate_postfix("12345 * + * +"))

"""
3 + 4 => +34
"""
def dq_evaluate_prefix(prefix_expr):
    
    """
    1. add numbesr to stack
    2. whne you reach an operator 
            pop the stack twice
    3 perform the math of the opeartor
    """    
    
    print(prefix_expr)
    
    op_stack = Stack()
    
    numeral_tokens = \
    "0123456789"
    
    operator_tokens = \
    "+-*/"
        
    import operator
    
    operator_to_fn_map = \
    {
     "+" : operator.add,
     "*" : operator.mul,
     "-" : operator.sub,
     "/" : operator.__truediv__,
    }
    
    #start parsing
    for token in prefix_expr[::-1]:
        
        print("Stack -> %s" %(op_stack.items))
        
        #case operand
        if token in numeral_tokens:
            op_stack.push(token)
            
        #case operator
        elif token in operator_tokens:
            
            second_operand = \
            op_stack.pop()
            
            first_operand = \
            op_stack.pop()
            
            #perform math
            operator_fn = \
            operator_to_fn_map[token]
            
            result = \
            operator_fn(
                    int(first_operand),
                    int(second_operand)
                    )
            #push result to stack
            op_stack.push(result)
            
    return op_stack.pop()

print(dq_evaluate_prefix("+34"))
prefix_exp = "*+345"
print(
      "%s => %s" %( prefix_exp, dq_evaluate_prefix(prefix_exp)
      ))
prefix_exp = "+3*45"
print(
      "%s => %s" %( prefix_exp, dq_evaluate_prefix(prefix_exp)
      ))


def dq_infix_to_prefix_two_stacks_method(infix_expr):
    
    #precedence table
    prec = {}
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec[")"] = 1
    
    alaphabet_tokens = \
    "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    numeral_tokens = \
    "0123456789"
    
    #stack to hold operators
    op_stack = Stack()
    
    #list to hold operands
    #and final result
    prefix_stack = Stack()
    
    #split the expression
    tokens_list = \
    infix_expr.split()
    
    #print("tokens_list %s" %(tokens_list))
    
    # evaluate the expression
    # we start evaluating left to right
    # 1. reverse the list
    tokens_list_reversed = \
    tokens_list[::-1]
    
    #expression enumration begin
    for token in tokens_list_reversed:
        #2. case ")"
        # since we start from the end of the expression
        # we consider "(" to be end of the grouping
        if token is ")":
            op_stack.push(token)
            
        #3.case operand 
        elif token in alaphabet_tokens or \
        token in numeral_tokens:
            prefix_stack.push(token)
            
        #4. case "("
        elif token is "(":
            # marks the end of expression or
            # closing of  a grouping ()
            # move all operators till "(" to output
            
            
            top_operator = \
            op_stack.pop()
            
            while not  top_operator is ")":
                prefix_stack.push(top_operator)
                top_operator = \
                op_stack.pop()
                
        else:
            
            #ie. for +,*,-./
            # compare with all ops in the op_stack
            # find out if there is any operator with higher precedence
            # if yes add all of them to output
            # push to op_stack
                    
            while not op_stack.is_empty() and \
            prec[op_stack.peek()] >= prec[token]:
                
                #move them to output
                operator = \
                op_stack.pop()
                
                prefix_stack.push(operator)
                
            #if op_stack is empty    
            #push the operator to op_stack
            op_stack.push(token)    
            
       #expression enumration complete
       
    #move the remaining items
    while not op_stack.is_empty():
           
       operator = \
       op_stack.pop()
            
       prefix_stack.push(operator)
           
    #join the string
    a = lambda stack: array = []  
    return " ".join()