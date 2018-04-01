# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 01:45:13 2018

@author: sanooj
"""

"""
4.2.1 Calculating the Sum of a List of Numbers
"""

def list_sum(num_list):
    the_sum = 0
    
    for element in num_list:
        the_sum = the_sum + element
        
    return the_sum

print("sum %s" %(list_sum([1,3,5,7,9])))


def list_sum_recursion(num_list,iteration = None):
    
    if iteration == None:
        iteration = 0
    else:    
        iteration = iteration + 1
    
    print(iteration)
    print(num_list)
    
    if len(num_list) == 1:
        return num_list[0]
    else:
        return (
                num_list[0] +
                list_sum_recursion(num_list[1:],iteration
                                   )
                )
    
print("sum %s" %(list_sum_recursion([1,3,5,7,9])))

def compute_factorial(number):
    
    if number == 1:
        return number
    elif number < 1:
        return 1
    else:
        return (
            number * compute_factorial(number - 1)
            )
        
print("factorial of %s is %s" %(0, compute_factorial(0)))


def to_str(n, base):
    
    string_lookup = "0123456789ABCDEF"
    
    if n < base:
        return string_lookup[n]
    else:
        quotient = n // base
        reminder = n % base
        print("quotient = %s" %(quotient))
        print("reminder = %s" %(reminder))
        return (
                to_str(quotient , base) +
                string_lookup[reminder]
                )
        
#print(to_str(1453, 16))
print(to_str(2, 2))


"""
SELF CHECK
"""

"""
Self Check
Write a function that takes a string as a parameter 
and returns a new string that is the reverse of
the old string
"""
def revesre_string_via_recursion(string):
    
    print(string)
    
    #base case
    if len(string) <= 1:
        return string
    else:
        
        #first_char
        first_char = string[0]
        
        #remaining string after excluding the first char
        nu_string = string[1:]
        
        #since recursion happens first
        #number of recursions will be same as len(string) - 1
        #and inner loop will exit first
        return (
                revesre_string_via_recursion(
                        nu_string
                        ) + 
                        first_char
                )
                
print(revesre_string_via_recursion("kayak"))
print(revesre_string_via_recursion("sanooj"))

"""
Write a function that takes a string as a parameter and 
returns True if the string is a palindrome,
False otherwise. Remember that a string is a palindrome
 if it is spelled the same both forward
and backward. for example: radar is a palindrome.
 for bonus points palindromes can also be
phrases, but you need to 
remove the spaces and punctuation before checking.
 for example:
madam i’m adam is a palindrome. 
Other fun palindromes include:
• kayak
• aibohphobia
• Live not on evil
• Reviled did I live, said I, as evil I did deliver
• Go hang a salami; I’m a lasagna hog.
• Able was I ere I saw Elba
• Kanakanak – a town in Alaska
• Wassamassaw – a town in South Dakota
4.3 Stack
"""

def strip_characters(string, stringToStrip):
    
    new_string = string
    
    for element in stringToStrip:
        new_string = \
        new_string.replace(element,"")
        
    return new_string

def test_strip_characters():
    
    string = "they are idiots, nond, ssadd '"
    print(strip_characters(string," ,'"))

test_strip_characters()

def strip_characters_via_recursion(string, stringToStrip):
    
    #print("string => [%s]" %(string))
    #print("stringToStrip => [%s]" %(stringToStrip))
    
    #base
    if len(string) <= 1:
        #check condition for last character
        if string in stringToStrip:
            return ""
    
    #recurse
    reduced_string = string[1:]
    new_string = string[0]
    
    #print("new_string => [%s]" %(new_string))
    
    #check condition for every character except last
    #replace string with replacement char
    # here it is ""
    if new_string in stringToStrip:
        new_string = ""
        
    return (
             new_string +
             strip_characters_via_recursion(
                     reduced_string, stringToStrip
                     )
            )
    
def test_strip_characters_via_recursion():
    
    #string = ", non + d, +"
    string = "they are idiots, nond, ssadd '"
    print(strip_characters_via_recursion(string," ,+'"))
    
test_strip_characters_via_recursion()

def is_a_palindrome_via_recursion(
        string , 
        start_index, 
        end_index):
    
    print("start_index %s" %(start_index))
    print("end_index %s" %(end_index))
    
    #base
    if start_index == end_index:
        return True
    
    #first and last
    if string[start_index] is not string[end_index]:
        return False
    
    if start_index < end_index + 1:
        return is_a_palindrome_via_recursion(
                string, 
                start_index + 1,
                end_index - 1
                )
        
    return True

def is_a_palindrome(string):
    
    start_index = 0
    end_index = len(string) - 1
    
    while start_index < end_index :
        
        if string[start_index] is not string[end_index]:
            return False
        else:
            start_index = start_index + 1
            end_index = end_index - 1
        
    return True
        

def test_is_a_palindrome_via_recursion():
    
    string = "kayak"
    print(
            is_a_palindrome_via_recursion(
                    string,
                    0,
                    len(string) - 1
                    )
            )
    
test_is_a_palindrome_via_recursion()

def test_is_a_palindrome():
    
    string = "kayak"
    print(is_a_palindrome(string))
    
test_is_a_palindrome()
