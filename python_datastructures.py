# -*- coding: utf-8 -*-
"""
Created on Sun May 14 16:28:50 2017

@author: sanooj
"""

"""
LIFO - Last In First Out

push
pop
peek
"""
class p_stack:
    def __init__(self):
        self.items = []
        
    def is_empty(self):
        return (len(self.items) == 0)
    
    def push(self,item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def peek(self):
        return self.items[len(self.items) - 1]
    
    def size(self):
        return len(self.items)
    
    def example_usage():
        stack = p_stack()
        for i in [1,2,3]:
            stack.push(i)
        print(stack.pop())
        print(stack.peek())
        print("stack.items") 
        print(stack.items)   
        print(stack.is_empty()) 
    """
    check If paranthesese match
    (((())))
    """
    
p_stack.example_usage()

"""
if __name__ == "__main__":
    # execute only if run as a script
""" 

def par_checker_mine(symbol_string):
        count_of_open = 0
        count_of_closed = 0
        
        char = ""
        for char in symbol_string:
            if char == "(":
                count_of_open = count_of_open + 1
            
            if char == ")":
                count_of_closed = count_of_closed + 1
                
        if count_of_open == count_of_closed:
            print(True)
        else:
            print(False)
        print(count_of_open)
        print(count_of_closed)

print("par_checker_mine(\"(())\")")
par_checker_mine("(())")

def par_checker_stack(symbol_string):
    s = p_stack()
    
    index = 0
    is_balanced = True
    
    while index < len(symbol_string) and is_balanced:
        print(s.items)
        c_symbol = symbol_string[index]
        if c_symbol == "(":
            s.push(c_symbol)
        else:
            if s.is_empty():
                #print(False)
                is_balanced = False
            else:
                 print("s.pop()")
                 print(s.pop())
        
        index = index + 1
    
    print(s.items)
    
    if s.is_empty and is_balanced:
        return True
        #print(True)
    else:
        return False
        print("FFTrue")

print(par_checker_stack("(())"))

def par_checker(symbol_string):
    s = p_stack()
    balanced = True
    index = 0
    while index < len(symbol_string):
        symbol = symbol_string[index]
        if symbol == "(":
            s.push(symbol)
        if symbol == ")":
            s.pop()

        index = index + 1

    if s.is_empty():
        return True
    else:
        return False

print(par_checker('((()))'))
print(par_checker('(()'))
#"""    


"""
DIVIDE By two
to Convert Decimal to binary
"""
def convert_decimal_to_binary(decimal_number):
    rem_stack =  p_stack()
    
    while decimal_number > 0:
        rem = decimal_number % 2
        rem_stack.push(rem)
        
        decimal_number = decimal_number
        
    bin_string = ""
    while not rem_stack.is_empty():
        bin_string = bin_string + str(rem_stack.pop())
    
    
    return bin_string
print(convert_decimal_to_binary(8))
        
