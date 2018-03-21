# -*- coding: utf-8 -*-
"""
Created on Fri Feb 23 19:26:12 2018

@author: sanooj
"""

from DataStructures import Stack

"""
Exercises
Given the following sequence
 of stack operations, 
 what is the top item on the stack
 when the
sequence is complete?
m = Stack.Stack()
m.push('x')
m.push('y')
m.pop()
m.push('z')
m.peek()
"""

class StackExercises:
    
    def testingOperations():
        print("testingOperations")
        m = Stack.Stack()
        m.push('x')
        m.push('y')
        m.debug_print()
        m.pop()
        m.debug_print()
        m.push('z')
        m.debug_print()
        print(m.peek())
        
    def testingLoopingScenario():
        m = Stack.Stack()
        m.push("x")
        m.push("y")
        m.push("z")
        while not m.is_empty():
            m.pop()
            m.pop()

StackExercises.testingOperations()
#error  testingLoopingScenario
#StackExercises.testingLoopingScenario()

"""
Balancing parntheses

"testing (()(()))

"""
class BalancingParantheses:
    
    def testingMyApproach():
        open_brace = '('
        close_brace = ")"
        
        stack =  Stack.Stack()
        
        string_to_test = "((()))"
        
        for index in range(0,len(string_to_test)):
            char = string_to_test[index]
            if char == open_brace:
                stack.push(char)
                print("push")
                print(stack.items)
            if char == close_brace:
                stack.pop()
                print("pop")
                print(stack.items)
        
        print(stack.is_empty())
        
    def par_checker(symbol_string):
        s = Stack.Stack()
        balanced = True
        index = 0
        while index < len(symbol_string) and balanced:
            symbol = symbol_string[index]
            if symbol == "(":
             s.push(symbol)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    s.pop()
            
            index = index + 1
        
        if balanced and s.is_empty():
             return True
        else:
             return False
         
            

BalancingParantheses.testingMyApproach()
print(BalancingParantheses.par_checker('((()))'))
print(BalancingParantheses.par_checker('(()'))


print("BalancingALotOfSymbols")

class BalancingALotOfSymbols:
    
    def matches(open_brace,close_brace):
        print("open_brace %s" %(open_brace))
        print("close_brace %s" %(close_brace))
        opens = "([{"
        closes = ")]}" 
        return (opens.index(open_brace) == 
     closes.index(close_brace))
    
    
    def testingMyApproach(string_to_test):
        open_braces = '({['
      
        stack =  Stack.Stack()
        
        for index in range(0,len(string_to_test)):
            char = string_to_test[index]
            
            if char in open_braces:
                stack.push(char)
            else:
                top = stack.pop()
                if not BalancingALotOfSymbols.matches(top,char):
                    stack.push(top)
        
        print(stack.is_empty())
                    
    # Completed extended par_checker for: [,{,(,),},]

    def par_checker(symbol_string):
        
        def matches(open, close):
            opens = "([{"
            closes = ")]}"
            return opens.index(open) == closes.index(close)
        
        s = Stack.Stack()
        balanced = True
        index = 0
        while index < len(symbol_string) and balanced:
            symbol = symbol_string[index]
            if symbol in "([{":
                s.push(symbol)
            else:
                if s.is_empty():
                    balanced = False
                else:
                    top = s.pop()
                    if not matches(top, symbol):
                        balanced = False
            index = index + 1                
                    
        if balanced and s.is_empty():
            return True
        else:
            return False
        
    def parantheses_checker_rewrite(symbol_string):
      isBalanced = True
      stack = Stack.Stack()
      open_chars = "({["
      
      def is_a_match(open_char,close_char):
        open_chars = "({["
        close_chars = ")}]"
        
        if open_chars.index(open_char) == close_chars.index(close_char):
          return True
        else:
          return False
        
      #enumerate the string  
      for char in symbol_string:
        if char in open_chars:
          stack.push(char)
        else:
          #check if stack is is_empty
          if stack.is_empty():
            isBalanced = False
          else:
            poppedVal = stack.pop()
            if is_a_match(poppedVal,char):
              #match
              pass
            else:
              isBalanced = False
      
      print(isBalanced)
      print(stack.items)
      
      if isBalanced and stack.is_empty():
        return True
      else:
        return False


BalancingALotOfSymbols.testingMyApproach("{[(])}")

print("Decimal-To-Binary")
def convertDecimalToBinary(decimal_number):
  """
  Implemneting the divide by 2 algorithm
  1. Modulus the given number by 2
    1.1 Compute the quotient (integer division)
  2. add the reminder to a stack
  3. keep on dividing the quotient untill the quotient is  < 2
  """
  
  binary_number_stack = Stack()
  quotient = decimal_number
  
  while quotient >=2:
    reminder = quotient % 2
    binary_number_stack.push(reminder)
    quotient = quotient // 2
  
  #add final quotient to stack
  binary_number_stack.push(quotient)
  
  #reverse to get the binary number
  binary_number_stack.items.reverse()
  
  print(binary_number_stack.items)
  
convertDecimalToBinary(7) #111
convertDecimalToBinary(8) #1000  
convertDecimalToBinary(9) #1001

print("Decimal-To-Anybase")
def convertDecimalToAnyBase(decimal_number,base):
  """
  Implemneting the divide by 2 algorithm
  1. Modulus the given number by 2
    1.1 Compute the quotient (integer division)
  2. add the reminder to a stack
  3. keep on dividing the quotient untill the quotient is  < 2
  """
  
  binary_number_stack = Stack()
  quotient = decimal_number
  
  while quotient >= base:
    reminder = quotient % base
    binary_number_stack.push(reminder)
    quotient = quotient // base
  
  #add final quotient to stack
  binary_number_stack.push(quotient)
  
  #reverse to get the binary number
  binary_number_stack.items.reverse()
  
  print(binary_number_stack.items)
  
convertDecimalToAnyBase(7,2) #111
convertDecimalToAnyBase(8,2) #1000  
convertDecimalToAnyBase(9,2) #1001
convertDecimalToAnyBase(9,2) #1001

print("Decimal-To-Hex")
def convertDecimalToHex(decimal_number, base = 16):
  hex_digit_set = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
  
  oct_digit_set = [0,1,2,3,4,5,6,7]
  
  binary_number_stack = Stack()
  quotient = decimal_number
  
  digit_set = []
  if base == 16:
    digit_set = hex_digit_set
  if base == 8:
    digit_set = oct_digit_set
  
  #perform divide_by_base
  while quotient >= base:
    reminder = quotient % base
    binary_number_stack.push(reminder)
    quotient = quotient // base
  
  #add final quotient to stack
  binary_number_stack.push(quotient)
  
  #reverse to get the binary number
  binary_number = binary_number_stack.items[:]
  binary_number.reverse()
  
  #get the HEX digit from hex_digit_set
  last_binary_digit = binary_number[len(binary_number) - 1]
  print(last_binary_digit)
  
  hex_digit = digit_set[last_binary_digit]
  print(hex_digit)
  
  #modify the list returned after dividing by base
  binary_number.pop()
  print(binary_number)
  
  #add the Hex digit insteda of the reminder
  binary_number.append(hex_digit)
  print("hex_number %s" %(binary_number))
  
  print(binary_number_stack.items)
  
convertDecimalToHex(256) #100
convertDecimalToHex(256,8) #400


#Convert infix to post fixx
"""
Rules 
1. 
"""


def infix_to_postfix(infix_expr):
    
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
    op_stack = Stack.Stack()
    
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
        
        while not op_stack.is_empty():
            
            #get operator
            oper = op_stack.peek()
            
            #get precedence
            oper_prec = prec[oper]
            
            #get precedence of current token
            token_prec = prec[token]
            
            #compare
            if oper_prec >= token_prec:
                
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
        

def infix_to_postfix1(infix_expr):
  
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
    op_stack = Stack.Stack()
    
    #list to hold operands
    #and final result
    postfix_list = []
    
    #split the expression
    tokens_list = \
    infix_expr.split()
    
    #enumerate
    for token in tokens_list:
      #check if token in alpabet or numeral_tokens
      if token in alaphabet_tokens or token in numeral_tokens:
        #push to postfix_list
        postfix_list.append(token)
      #check for open braces "("
      #this is a operator
      elif token == "(":
        #add to op_stack
        op_stack.push(token)
      #check for closing braces ")"
      elif token == ")":
        """
        1. this is also an operator
        2. indicating end of an expression
        3. Logic to make an infix postfix is to move the operator to where the closing bracket is 
        4. this takes into account operator precedence
        5. (A + B) * C for eg in postfix is AB+C*
        6. A + (B * C) is ABC*+ 
        
        """
        #get operator
        op_from_stack = op_stack.pop()
        #pop the stack untill we get an open braces
        #which indicates beginning of the expression 
        while not op_from_stack == "(":
          #append to the answer
          postfix_list.append(op_from_stack)
          #pop to continue while loop
          op_from_stack = op_from_stack.pop()
      
      #operator found (+,-,/,*)
      else:
        
        #push to op stack if it is empty
        if op_stack.is_empty():
          op_stack.push(token)
        else:
          #loop
          while op_stack.is_empty():
            #precedence comparison
            #if "token" precedence >= precedence of element in 
            #stack 
            # pop the stack and appane it to the output
            # 
            if prec[token] >= prec[op_stack.peek()]:
              postfix_list.append(op_stack.pop())
    #enumeration done
    
    #empty the op_stack
    # as we only emptied the ops with lesser precedence
    while not op_stack.is_empty():
      postfix_list.append(op_stack.pop())
      
    #make the String
    return " ".join(postfix_list)
    

#postfix evaluation
def evaluating_a_prefix(postfix_expr):
    
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
    
    op_stack = Stack.Stack()
    
    for token in postfix_expr:
        if token in numeral_tokens:
            op_stack.push(token)
        
        if token in operator_tokens:
            second_operand = \
            op_stack.pop()
            
            first_operand = \
            op_stack.pop()
            
            result = \
            operator_to_fn_map[token](
                              int(first_operand), 
                              int(second_operand))
            
            op_stack.push(result)
    
    return op_stack.pop()
    
print(evaluating_a_prefix('78+32+/'))  


def postfix_eval(postfix_expr):
    operand_stack = Stack.Stack()
    token_list = postfix_expr.split()
    for token in token_list:
        if token in "0123456789":
            operand_stack.push(int(token))
        else:
            operand2 = operand_stack.pop()
            operand1 = operand_stack.pop()
            result = do_math(token, operand1, operand2)
            operand_stack.push(result)
    return operand_stack.pop()
    
def do_math(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2
print(postfix_eval('7 8 + 3 2 + /'))