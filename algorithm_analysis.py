# -*- coding: utf-8 -*-
"""
Created on Tue May  2 14:20:52 2017

@author: sanooj
"""

#Algoritm anlaysis

# sumof n digits

def useThis():
    def sum_Of_v(n):
        sum = 0
        for element in range(1,n+1):
            #print(element)
            sum += element
        print(sum)
   
    import time
    start = time.time()
    sum_Of_v(10000000)
    end = time.time()
    
    print(end-start)
    
    
    def sum_using_equation(n):
        # i = (n* n+1) / 2
        return (n * (n+1)) / 2
    start = time.time()
    print(sum_using_equation(10000000))
    end = time.time()
    print(end-start)
    
    """
    Analysis big(O)
    order of magnitude
    """
    def analysis(n):
        a = 5
        b = 6
        c = 10
        for i in range(n):
            for j in range(n):
                x = i * i
                y = j * j
                z = i * j
        for k in range(n):
            w = a * k + 45
            v = b * b
        d = 33
        
        """
        Couting the number of assignment
         3
         2 loops one inner so n^2
         3rd loop 2 assignments 
         n
         constnat assignments 
         4
         
         f(n) = 3n^2 + 2n + 1
         
         O(f(n)) =  n^2
         as for larger values of n^2 
         contributes the most
         
         
         
        """
    
    def minimum_number_in_a_list(lista):
        for i in range(len(lista)):
            for j in range(len(lista)-1):
                if lista[j + 1] > lista[i]:
                    temp1 = lista[i]
                    temp2 = lista[j+1]
                    lista[j+1] = temp1
                    lista[j] = temp2
        print(lista)
    
    minimum_number_in_a_list([3,1,9])
    
    
    def anagram_solution1(s1,s2):
        a_list = list(s2)
        
        pos1 = 0
        still_ok =  True
        
        while pos1 < len(s1) and still_ok:
            pos2 = 0
            found = False
            
            while pos2 < len(a_list) and not found:
                if s1[pos1] == a_list[pos2]:
                    found = True
                else:
                    pos2 = pos2 + 1
           
            if found:
                a_list[pos2] =  None
            else:
                still_ok = False
                
            pos1 = pos1 + 1
            
        return still_ok     
    
    print(anagram_solution1('abcd','dcba'))
    
    
    def anagram(char = "goog"):
        char_length = len(char)
        match = False
        for index_1 in range(0,char_length-1):
            for index_2 in range(char_length-1,0,-1):
                print(char[index_1])
                print(char[index_2])
                if char[index_1] == char[index_2]:
                    match = True
                else:
                    match = False
        print("anagram")            
        print(match)    
            
    anagram("ana")
    
    def check_if_an_anagram(first_word,second_word):
        char1_length = len(first_word)
        char2_length = len(second_word)
        match = False
        if char1_length == char2_length:
            for index_1 in range(0,char1_length-1):
                for index_2 in range(0,char2_length -1):
                    if first_word[index_1] == second_word[index_2]:
                        match = True
                    else:
                        match = False
        print("check_if_an_anagram")            
        print(match)
   
    check_if_an_anagram("malayalam","malayalam")
   
    """
    #Count and compare solution
    #every character will occur exactly the same number of times in both 
    #words
    #26 letters in English alphabet
    #2 arrays of length 26
    each array index denoting the count of a character
    """
    
    def anagaram_solution_count_and_compare(s1,s2):
        c1 = [0] * 26
        c2 = [0] * 26
        
        for i in range(len(s1)):
            print("check_if_an_anagram")
            print(ord(s1[i]))
        print(ord('a'))
        print(ord('z'))
        print(ord('z') - ord('a'))
        
        """
        subtract ascii of 'a' from any letter 
        """
        for i in range(len(s1)):
            pos = ord(s1[i]) - ord('a')
            c1[pos] = c1[pos] + 1
       
        for i in range(len(s2)):
            pos = ord(s2[i]) - ord('a')
            c2[pos] = c2[pos] + 1
            
        j = 0
        still_ok = True
        while j < 26 and still_ok:
            print("j = %d" % j)
            if c1[j] == c2[j]:
                j = j + 1
            else:
                print("j at else = %d" % j)
                still_ok = False
                
        return still_ok        
   
    print(anagaram_solution_count_and_compare("maalyalam","malayalam"))


    def adssd():
        def anagarm_aray_logic_reimplemented(s1,s2):
          list1 = [x * 0 for x in range(1,27)]
          list2 = [x * 0 for x in range(1,27)]
          
          """
          lopp through all characters
          increment 1 in for each postion
          wgne you find a character in that position
          in English alpabet
          """
          for i in s1:
              pos1 = ord(i) - ord('a')
              list1[pos1] = list1[pos1] + 1
    
          for j in s2:
              pos1 = ord(j) - ord('a')
              list2[pos1] = list2[pos1] + 1
         
          print(list1)
         
          print(list2)
          
          """
          Check if both lists are equal
          """
          a = 0
          ok = False
          while a < len(list1):
              if list1[a] == list2[a]:
                  a = a + 1
                  ok = True
              else:
                  ok = False
          print(a)        
          print(ok)
          if a == len(list1):
              print(True)
          else:
              print(False)
         
        anagarm_aray_logic_reimplemented("maalyalam","malayalam")
  
    #adssd()
    def anagarm_reimplemented(s1,s2):
          list1 = [x * 0 for x in range(1,27)]
          list2 = [x * 0 for x in range(1,27)]
          
          """
          lopp through all characters
          increment 1 in for each postion
          wgne you find a character in that position
          in English alpabet
          """
          for i in s1:
              pos1 = ord(i) - ord('a')
              list1[pos1] = list1[pos1] + 1
              
          print(list1)   
          
          def anagram(char = "goog"):
            char_length = len(char)
            match = 0
            for index_1 in range(0,char_length-1):
                for index_2 in range(char_length-1,0,-1):
                    print("char[index_1] = %s" % char[index_1])
                    print("char[index_2] = %s" % char[index_2])
                    if char[index_1] == char[index_2]:
                        match = match + 1
                    else:
                        match = 0
            print("anagram")            
            print(match) 
            """
            if match % 2:
                print(match)
            else:
                print(match)
            """
            print(len(char))
            if len(char) % 2:
                print(match == (len(char) / 2))
            else:
                print(match == ((len(char) - 1) / 2) )
          anagram(s1)
        
    anagarm_reimplemented("malayalam","malayalam")       

    def anagarm_reimplemented_true(s1,s2 = ""):         
          
          s1_size = len(s1)
          s2_size = len(s2)
        
          print("s1_size = %s" % (s1_size))
          print("s2_size = %s" % (s2_size))
          
          if len(s1) != len(s2) and s2 != "":
              print(False)
              return False
              
          dict1 = {}
          dict2 = {}

          pos = 1
          for char in s1:
              dict1["%d"  % (pos)] = char
              pos = pos + 1
          
          pos = 1
          if s2 == "" :
              s2 = s1
              
          for index in range(len(s2) ,0 ,-1):
              dict2["%d"  % (pos)] = s2[index - 1]
              pos = pos + 1
          
          count = 0  
          for key in dict1:
              if dict1[key] == dict2[key]:
                  count = count + 1
              print(key)
              
          print(count)        
          print(dict1)
          print(dict2)
          
          if count == len(dict1) and count == len(dict2):
              print(True)
              return True
          else:
              print(False)
              return False
              
    print(anagarm_reimplemented_true("malayalam"))       
useThis()    