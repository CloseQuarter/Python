# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 09:56:42 2017

@author: sanooj
"""

"""
#Array Left Rotation

A left rotation operation on an array of size 
 shifts each of the array's elements  unit to the left.
 For example, if  left rotations are performed on array [1,2,3,4,5] , 
 then the array would become . [3,4,5,1,2]
 

Given an array of  integers and a number, , perform  left rotations on the array.
 Then print the updated array as a single line of space-separated integers.
"""

def print_on_demand(didDemand,*args):
    if didDemand:
        print(args)

class ArrayRotation():
    def use_array_left_rotation():
        tmp_array = [1,2,3,4,5]
        print(tmp_array)
        
        def array_left_rotation(a, n, k):
            for index in range(0,k):
                first_obj = a[0]
                a.pop(0)
                a.append(first_obj)
            return a    
        
        print(array_left_rotation(tmp_array,5,4)) 
        
        print(tmp_array)
        
    def arrayRotation(array,array_size,times):
    
        """preconditions"""
        if array_size == 0:
            return None
        
        if len(array) == 0:
            return None
        
        if times < 0 or array_size < 0:
            return None
        
        def shift_an_array_to_left(array,shift_range):
            for index in shift_range:
                array[index] = array[index+1]
            return array
        
        for shift_count in range(0,times):
            first_index = 0
            first_object = array[first_index]
            for index in range(first_index,array_size - 1 - first_index):
                ##shift all objects one position to left
                array[index] = array[index + 1] 
            
            #update last index
            array[array_size - 1] = first_object
        


    

ArrayRotation.use_array_left_rotation()



"Strings: Making Anagrams"
"""
Given two strings, a and b , that may or may not be of the same length,
 determine the minimum number of character deletions required to make 
 and  anagrams.
 Any characters can be deleted from either of the strings.
"""

class MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram():
    
  def sort_string(string):
        sorted_strings = sorted(string)
        return sorted_strings 
        
  #dicts
  def make_dict_with_char_count(string):
      dict_with_char_count = {}
      for char in string:
        if char in dict_with_char_count:
            tmpCount = dict_with_char_count[char]
            tmpCount = tmpCount + 1
            dict_with_char_count[char] = tmpCount
        else:
            dict_with_char_count[char] = 1
      return dict_with_char_count          
              
  def sum_of_dict(dictionary):
      sum_of_values = 0
      for index,key in enumerate(dictionary):
          value = dictionary[key]
          print("key: " + str(key) + " " + "value: " + str(value))
          sum_of_values =  sum_of_values + int(value)
      return sum_of_values    
                         
  def number_needed_count_approach(a, b):
        dict_a = MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.make_dict_with_char_count(a)
        print(dict_a)
        
        dict_b = MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.make_dict_with_char_count(b)
        print(dict_b)
        
        alphabets_upperCase = map(chr,range(65,91))
        alphabets_lowerCase = map(chr,range(97,123))
        
        result = 0
        print(alphabets_lowerCase)
        for alphabet in alphabets_lowerCase:
             #https://wiki.python.org/moin/KeyError
            count_a = dict_a.get(alphabet,0)
            count_b = dict_b.get(alphabet,0)
            
            print("count_a %s  :  %d \n"% (alphabet,count_a))
            print("count_b %s  :  %d \n" % (alphabet,count_b))
            print("result  %d \n" % (result))
            print(" count_a - count_b = %d" %(count_a - count_b))
            
            result = result + abs(
                    count_a - count_b
                    )
            
            #print(alphabet)
            print(result)
        sum_of_dict_a = MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.sum_of_dict(dict_a)
        sum_of_dict_b = MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.sum_of_dict(dict_b)
        
        print(sum_of_dict_a)
        print(sum_of_dict_b)
        
        print("result " + str(result))
        
        return result
        
  
  #unused            
  def number_needed(a, b):
        sorted_a = sorted(a)
        sorted_b = sorted(b)
        
        print("sorted_a %s" , sorted_a)
        print("sorted_b %s" ,sorted_b)
        
        if sorted_a == sorted_b:
            print(1)
        else:
            print(0)
            """
            1. make sets
            2. find unique elements in both
            3. get their count
            """
            sorted_set_a = set(sorted_a)
            sorted_set_b = set(sorted_b)
            
            difference_set = sorted_set_a.symmetric_difference(sorted_set_b)
            
            print(sorted_set_a.difference(sorted_set_b))
            print(difference_set)
            
        return len(difference_set)
    
  #print(number_needed("fsqoiaidfaukvngpsugszsnseskicpejjvytviya","ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"))
   
"""
  number_needed_count_approach(
       "fsqoiaidfaukvngpsugszsnseskicpejjvytviya",
       "ksmfgsxamduovigbasjchnoskolfwjhgetnmnkmcphqmpwnrrwtymjtwxget"
       )
"""       

  #MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.number_needed_count_approach("bcadeh","hea")
  
print(MinimumNumberofCharactersToBeRemovedFromAStringToMakeAnAnagram.number_needed_count_approach("bcadeh","hea"))

#print(sort_string("dasdfg"))


"""
Given the words in the magazine and the words in the ransom note,
 print Yes if he can replicate his ransom note exactly using whole words
 from the magazine; otherwise, print No.
"""
class RansomNote():
    def ransom_note(magazine, ransom):
        magazine_words = magazine.split(" ")
        print(magazine_words)
        
        ransom_words = ransom.split(" ")
        print(ransom_words)
        
        magazine_dict = RansomNote.make_dict_with_word_count(magazine_words)
        ransom_dict = RansomNote.make_dict_with_word_count(ransom_words)
        
        return RansomNote.check_if_word_counts_match(magazine_dict,ransom_dict)
        
      #dicts
    def make_dict_with_word_count(wordArray):
        dict_with_char_count = {}
        for word in wordArray:
            
            print(word)
            
            current_word_count = dict_with_char_count.get(word,0)
            print(current_word_count)
            
            current_word_count = current_word_count + 1
            print(current_word_count)
            
            dict_with_char_count[word] = current_word_count
            
        print(dict_with_char_count)
        
        return dict_with_char_count
    
    def check_if_word_counts_match(magazine_dict,ransom_dict):
        count_matches = 0
        for index,key in enumerate(ransom_dict):
            if magazine_dict[key] >= ransom_dict[key]:
                count_matches += 1
            else:
                pass
        
        print(count_matches)
        print(len(ransom_dict))
        if count_matches == len(ransom_dict):
            return True
        else:
            return False

print(RansomNote.ransom_note(
        "two times three is not four four","two times two is four"
        ))


"""
Detect a cycle in a linked list. 
Note that the head pointer may be 'None' if the list is empty.
"""

class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node            

def has_cycle(head):
    #traverse
    visited_node_value = []
    current_node = head
    while current_node != None:
        current_node_value = current_node.data
        if current_node_value in visited_node_value:
            print("hasCycle")
            print(visited_node_value)
            return True
        else:
            visited_node_value.append(current_node_value)
        current_node = current_node.next
    return False   

def makeNodeVisitedCountDict():
    nodes = {}
    headNode = Node()
    headNode.data = 1
    headNode.next = None
    
    nodes[headNode] = 0
    
    currentNode = headNode
    
    for index in range(2,6):
        childNode = Node()
        childNode.data = index
        childNode.next = None
        currentNode.next = childNode
        currentNode = childNode
           
        nodes_count = nodes.get(childNode,0)
        nodes_count += 1
        
        nodes[childNode] = nodes_count
        
    print(nodes)    
    
    current_node = headNode
    while current_node != None:
        print(current_node.data)
        current_node = current_node.next
    
    return headNode
    
has_cycle(makeNodeVisitedCountDict())


"""
Stacks: Balanced Brackets
LIFO
The string {[()]} meets both criteria for being a balanced string, 
so we print YES on a new line.
The string {[(])} is not balanced, 
because the brackets enclosed by the matched pairs [(] and (]) 
    are not balanced. Thus, we print NO on a new line.
The string {{[[(())]]}} meets both criteria for being a balanced string, 
so we print YES on a new line.
"""

test = """
[]][{]{(({{)[})(}[[))}{}){[{]}{})()[{}]{{]]]){{}){({(}](({[{[{)]{)}}}({[)}}([{{]]({{
[]()([{}])[]{}[]
)}{){(]{)([)}{)]())[(})[]]))({[[[)}[((]](])][({[]())
{}()[[((()(({{[]}{}{{[]}}{}}))))]]{{{{([{{{{}}}}])}}}}
{{[()()]}()}(())()()[[[]]][{[]()}(())]
[}}{}]{[{)}[{(([)(([)(](}(]([}(()[)])}[{[{{](([]()[[[])([}}])){}(][)]{(]{)]]()({}}}(((]{]]
(}{(()[][[){{}{{[}][]{{{{[{{[](}{)}](}}()]}(}(}}]}[](]]){{{()}({[[}}{{[]}(]}{(]{}}[()(}]{[[]{){{
{}{[[[[[][]]]]({})]}[[]]
)}}}){}{](]}){}((]]{][)]({[{)])[{])}(]]][)[{[}()[}])}}}]}}})]))[
))())][})[{)]]})[({}[){)([])[}{}]{])({]{}}[(({({])]}
[{(((([]))({{}{}[]{{()}[({[{}[]]}[][([])[]]{})[{}(){{[{}({}{{}[]}{({})}{((({})))})(){}]}}]]}})))}]
)][)]}([]]))(]){}({{[]({{{({)]]}]{[}]]([)][[[()[][[}{}(]){(()[)[[[{]{)]}{{)[][()]{}(({]}])
{]({}[[)[}([][[[)]()(]((}}}{}){}{}{]({][(]}()[}}{[{[((])})]{}}](}[[[){(([)({()[{(}}({}{]][)}(}({([(]
{[])[))[)}}]}([}()}{{]}[)}{)}[}}]])}((((])[)[[()[{({](}]
{(){{}}}{}{{({})}}{({(){}})}
{}{([{{{{}})]{)]()[[}(}{
[[()]{{}[()[([])([]{}[])]]}]
{}))))((])({{[[}{])([})[([(]([)()(()(][](}]}])({]{()}[()(){[}(([[{{)}]]}(})((]}[([[()(
[]{()({}[[]])}{}[()[[]]][]
[][]{}({({})}({})()(){})
[[()({()([()])()}[][])]][]([](){}{[{{}{[]()}}{{()}}{}]})(){}[[[(([]))]][]{[][]{()}()[[()]]}]
}{)[(}]])[{)([()[})((}}]{]{{]([[]{{]([[{}[}(]]}({[{{))]][]]{}}])]([]())]](([}(}([[)}())([{
)}}[({}}]{
)()[(}}[{}[])))}({
({([{}{((){}()[])}])})
{][{(}[)()(}[)(]()(){))}]}]({)({}(}]
{]))}}{)[}}(]()[]))]](]}([{}]}(}[){])(
()])}{])(]})){){)){][}[{}[}[}[()[(({{{][[{}}{]]])}]([)][({
{[[[[([{}]{{}(){}}[]){}]]]][{}]{}()}{}()[[[(([])){[]}]]]{}(())(){[]{[(([]()()))]}}[([]){}()]{{[{}]}}
[[}]((({}()})[]][([(}]][
{{[]{}}}[{[]}[{}]{}][](()[])[][([([[({{(()(()()[[[[]()]()()]()]){})(([[]{}]))}})]]())])]
({]][[){[((([][[)[
}[]{{]}{[{]]}[]}}](}[]}[)]){{)](}]}]}]][(]}(((})])([{}
[({[][]}({{}[[{}{}()]]{()}}){{}[]{}{{()}}})]
[]{}{()}[[]]{}(([])){}{}()[]{}{[(()){}{()}]({}){({})}}[[{{}[()]}{()}]]{{}}{()}{}{{}[]}
[][{{[[{}(){}(())]{[{}]({})}]{}[[[{}[[]]]{}]]}}][([])([]())]
()}}}[)}([}})[(}
{(({}{}[{}()]{[]{}}))}
[][][{}]{()(()({{{[]}[(){[][[(){{}}][{}][]{()}[(([[]{}[[](()[[]])]]){()}[])(([]()))]]}]}}))}
(}(]}()(])()]}}{[]{(]]((]])}](}{}){{][[}{([[())([((}[](]([][[)})[[}[){[(}{]]][()[}
}]([([[[{}{](({([])){[)([([(}}}}[{})(}](()]((](])})}]])){]}{}]()]](]])]]]]
[(]){[}]}([[){){}[[}}}())})]})({](]{}([(][[]]()[[])}])
{{)))}])(({){])]}{}]{})[]){)}(]{])][]{(}{{{)}{{[((]][]){](]()}])][](((]{{{
){}[{())(]({]}]]){)]{((}{[{){[([([})]}])))}}[([([){({[[{}}{)}{
)(][()){}{[}[{[[{({})([{{{)({[([)]]][[{(){}[{}(}[[{])(({([[)({}{{)}())}}})[({}])[(({({{{})[)((
{[{{[[]]{}[{}]}{}}][](){}[[]]}[][](((({}))))[]{()}
({}){{}}[]{}{}[{}(){}][][]{}[({{{[()]}({}{{}}[[]()])}[{[([[]{()}()]){}]}]})]
})[)}[[[}(}[()])}([[)]()[)([{)(][)]})]{[}{({)))(()[)}[)[](
[]
[[([[]({[]}())])]](){}()()[]()[()][{}()](){[]}
{[[[})){}){}[[((]][{[({}([{{[({[)]{)])[[[{((]{){]{))(}({}[([({}){[(}{(]]{}[{)({]]{}}}()]([
[]{}[]{}[]({[{[]}]})
({}({}))()()({(())}{{[]}{}[]((([[[][([][[]{}(()())()][][({})][]{}[]()[](()){})]]])))})
{}}][[){(}{][}{{[))[(])(]][}{][}[)})({(][(}[{})[{){}
(([[({})]()][])()()[])
[({[(()[([{[][][]}])()]()[][])]})][](){{}[{}]}
]}[(][})))}{){(])[}]))()}[)][){({[{(]]]}[[]{)([{([)[{)[]][)((([[(([}
}{){{]})])}]
{([()][[{[[]()]}({()}){()[{()}]}]])}
[}[)]]]((]}){(](]{]]([)))][](]{]]]({{}]]]){)}})[()))({[[[([{}{))()[((]}]]{[}](}}}))}[[}[[{})
[()][]({}){}[]()[()]{(([]))[{}]}{}{}()[[](){}]()[{()()}{}][][({}[])]{}{}[]()
[][]()[]()({}){[{}[]{{}}{[]}[{(){[]{}()([][]())()}[[([])]]}]]}
[)[[[(]]{[{[]]
])}[{}][)]){(}))({([(}}[{{}[}](]{[][]()]([]{{{}})[))(]
()()[]{}[](){}[][]()[][][](()(())){}{{(){[[()]]{}{{}}}}}
}(}}
)})()([)[}){
(()){[[{}{{}}]]}
{()()}{{[][[[{[][()][(()){[{}{}(({()}))[()](){}][]}({([({})](){})})]{(()()[(([{}]))])}}]]]}}
(()){(){}[](()[])[]}()[[][]]()(){}{{}}()({}([({})([])])([[[]]][()])())()(){}[][{[([([{}{({})}])])]}]
[[]][{{}[]}][[]{}([(({{}}[]([]{})))()])((()[]))]{(){}{}}({})[[]{}]()[{}]()(){}[[(())[()]]]
(){}{()()((()([]{()}))[][({{{}{}()}[({}[(){}(()[[()[]]({}{}){}])]{})]}{})])}
{())))[[(]{[}(])()()[}}((][{[{))}{{}}[){]}()}(]{]]})}{[(][][((]]]}(}]}])])}})]{}]{]([)({
({]}]]
"""
def is_matched_alt(expression):
        push_stack_for_curlyOpen = []
        push_stack_for_squareOpen = []
        push_stack_for_paranthesesOpen = []
        pop_stack_for_paranthesesClosed = []
        pop_stack_for_squareClosed = []
        pop_stack_for_curlyClosed = []
        
    
        for index,char in enumerate(expression):
            if char == "{":
                push_stack_for_curlyOpen.insert(char)
            if char == "[":
                push_stack_for_squareOpen.append(char)
            if char == "(":
                push_stack_for_paranthesesOpen.append(char)
                
            if char == "}":
                pop_stack_for_curlyClosed.append(char)
            if char == "]":
                pop_stack_for_squareClosed.append(char)
            if char == ")":
                pop_stack_for_paranthesesClosed.append(char)
        
        #count all 
        
        if len(push_stack_for_curlyOpen) == len(
                pop_stack_for_curlyClosed
                ) and len(
                        push_stack_for_squareOpen
                        ) == len(
                                pop_stack_for_squareClosed
                                ) and len(
                                        push_stack_for_paranthesesOpen
                                        ) == len(
                                                pop_stack_for_paranthesesClosed
                                                ) :
            return True
        else:
            return False

def is_matched(expression):

        push_stack_for_curlyOpen = []
        push_stack_for_squareOpen = []
        push_stack_for_paranthesesOpen = []

        for char in expression:
            if char == "{":
                push_stack_for_curlyOpen.append(char)
            if char == "[":
                push_stack_for_squareOpen.append(char)
            if char == "(":
                push_stack_for_paranthesesOpen.append(char)
                
            if char == "}":
                if len(push_stack_for_curlyOpen) > 0:    
                    push_stack_for_curlyOpen.pop()
            if char == "]":
                if len(push_stack_for_squareOpen) > 0:
                    push_stack_for_squareOpen.pop()
            if char == ")":
                if len(push_stack_for_paranthesesOpen) > 0:
                    push_stack_for_paranthesesOpen.pop()
        
        #count all 
        
        if len(push_stack_for_curlyOpen
               ) > 0 or len(push_stack_for_squareOpen
               ) or len(push_stack_for_paranthesesOpen
               ) :
            return False
        else:
            return True

def is_matched_alt_2(expression):
        push_stack_for_curlyOpen = [0 for x in expression]
        push_stack_for_squareOpen = [0 for x in expression]
        push_stack_for_paranthesesOpen = [0 for x in expression]
        pop_stack_for_paranthesesClosed = [0 for x in expression]
        pop_stack_for_squareClosed = [0 for x in expression]
        pop_stack_for_curlyClosed = [0 for x in expression]
        
    
        for index,char in enumerate(expression):
            if char == "{":
                push_stack_for_curlyOpen.insert(index,char)
            if char == "[":
                push_stack_for_squareOpen.insert(index,char)
            if char == "(":
                push_stack_for_paranthesesOpen.insert(index,char)
                
            if char == "}":
                pop_stack_for_curlyClosed.insert(index,char)
            if char == "]":
                pop_stack_for_squareClosed.insert(index,char)
            if char == ")":
                pop_stack_for_paranthesesClosed.insert(index,char)
        
        #count all 
        
        
        for index,char in enumerate(push_stack_for_curlyOpen):
            if char == "{":
                pass
                
        
def is_matched_alt_1(expression):
    push_stack =  []
    pop_stack = []
    

    for index,char in enumerate(expression):
        if char == "{":
            push_stack.append(char)
        if char == "[":
            push_stack.append(char)
        if char == "(":
            push_stack.append(char)
            
        if char == "}":
            pop_stack.append(char)
        if char == "]":
            pop_stack.append(char)
        if char == ")":
            pop_stack.append(char)
    
    #count all 
    print("push %s" %(push_stack))
    print("pop %s" %(pop_stack))
  
    pop_stack.reverse()
    
    print("pop reverse %s" %(pop_stack))
    
    pop_stack_copy = pop_stack.copy()
    #print("pop copy %s" %(pop_stack_copy))
    
    #replace open with close
    for index,element in enumerate(pop_stack):
        if element == "}":
            pop_stack_copy[index] = "{"
        if element == ")":
            pop_stack_copy[index] = "("
        if element == "]":
            pop_stack_copy[index] = "["

    print(pop_stack_copy)
    
    if pop_stack_copy == push_stack:
        return (True)
    else:
        return (False)




def is_matched_alt_1_1_1(expression):
    
    #list of aacepted characters
    open_chars = ["{","[","<","("]
    close_chars = ["}","]",">",")"]
    
    #accepted char combination lookup tuple        
    curly = ("{","}")
    square =  ("[","]")
    angle = ("<",">")
    parantheses = ("(",")")

    #stack
    push_stack = []
    
    #loop through input
    for index,element in enumerate(expression):
        
        #open tag encountered
        if element in open_chars:
            push_stack.append(element)
        
        #close tag encountered
        if element in close_chars:
            if index == 0: #element begins with close char 
                return False
            else:
                # find out the last object in the stack
                # check if the last object in the stack's close counterpart 
                # matches current element
                
                if len(push_stack) > 0 and push_stack[len(push_stack) -1] == curly[0]:
                    if element == curly[1]:
                        #brackets match
                        #pop the stack
                        push_stack.pop()
                    else:
                        pass
                    
                if len(push_stack) > 0 and push_stack[len(push_stack) -1] == square[0]:
                    if element == square[1]:
                        #brackets match
                        #pop the stack
                        push_stack.pop()
                    else:
                        pass

                if len(push_stack) > 0 and push_stack[len(push_stack) -1] == angle[0]:
                    if element == angle[1]:
                        #brackets match
                        #pop the stack
                        push_stack.pop()
                    else:
                        pass

                if len(push_stack) > 0 and push_stack[len(push_stack) -1] == parantheses[0]:
                    if element == parantheses[1]:
                        push_stack.pop()
                    else:
                        pass
                    
    #print(push_stack)
    
    if len(push_stack) == 0:
            return True
    else:
            return False



class Stack:
     
    def __init__(self):
        self._data_store = []
        self.__top = -1
    
    def push(self,element):
        self._data_store.append(element)
        self.__top += 1 
        
    def pop(self):
        if len(self._data_store) > 0:
            self.__top -= 1 
            return self._data_store.pop()

    def isEmpty(self):
        return len(self._data_store) == 0        
    
    def count(self):
        return len(self._data_store)
    
    
    
"""rule.. last opened should be closed first"""
"""brackets should close"""
"""starts with closing braces - no match"""     
def is_matched_alt_1_1_1_1(expression):
    
    #list of aacepted characters
    open_chars = ["{","[","<","("]
    close_chars = ["}","]",">",")"]
    
    #accepted char combination lookup tuple        
    curly = ("{","}")
    square =  ("[","]")
    angle = ("<",">")
    parantheses = ("(",")")

    #stack
    push_stack = []
    
    #loop through input
    for index,element in enumerate(expression):
        
        #open tag encountered
        if element in open_chars:
            push_stack.append(element)
        
        #close tag encountered
        if element in close_chars:
            if index == 0: #element begins with close char 
                return False
            else:
                # find out the last object in the stack
                # check if the last object in the stack's close counterpart 
                # matches current element
                
                if len(push_stack) > 0 and element == curly[1]:
                    last_element = push_stack.pop()
                    if last_element == curly[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.append(element)
                        pass
                    
                if len(push_stack) > 0 and element == square[1]:
                    last_element = push_stack.pop()
                    if last_element == square[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.append(element)
                        pass
                    
                if len(push_stack) > 0 and element == angle[1]:
                    last_element = push_stack.pop()
                    if last_element == angle[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.append(element)
                        pass
                    
                    
                if len(push_stack) > 0 and element == parantheses[1]:
                    last_element = push_stack.pop()
                    if last_element == parantheses[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.append(element)
                        pass    
                    
    #print(push_stack)
    
    if len(push_stack) == 0:
            return True
    else:
            return False

def is_matched_alt_1_1(expression):
    
    #list of aacepted characters
    open_chars = ["{","[","<","("]
    close_chars = ["}","]",">",")"]
    
    #accepted char combination lookup tuple        
    curly = ("{","}")
    square =  ("[","]")
    angle = ("<",">")
    parantheses = ("(",")")

    #stack
    push_stack = Stack()
    
    #loop through input
    for index,element in enumerate(expression):
        
        #open tag encountered
        if element in open_chars:
            push_stack.push(element)
        
        #close tag encountered
        if element in close_chars:
            if index == 0: #element begins with close char 
                return False
            else:
                # find out the last object in the stack
                # check if the last object in the stack's close counterpart 
                # matches current element
                
                if (push_stack.count()) > 0 and element == curly[1]:
                    last_element = push_stack.pop()
                    if last_element == curly[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.push(element)
                        pass
                    
                if (push_stack.count()) > 0 and element == square[1]:
                    last_element = push_stack.pop()
                    if last_element == square[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.push(element)
                        pass
                    
                if (push_stack.count()) > 0 and element == angle[1]:
                    last_element = push_stack.pop()
                    if last_element == angle[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.push(element)
                        pass
                    
                    
                if (push_stack.count()) > 0 and element == parantheses[1]:
                    last_element = push_stack.pop()
                    if last_element == parantheses[0]:
                        #brackets match
                        #pop the stack
                        pass
                    else:
                        #put it back
                        push_stack.push(element)
                        pass    
                    
    #print(push_stack)
    
    if push_stack.count() == 0:
            return True
    else:
            return False         

print(is_matched_alt_1_1("}][}}(}][))]"))
print(is_matched_alt_1_1("[](){()}"))
print(is_matched_alt_1_1("()"))
#print(is_matched_alt_1_1("({}([][]))[]()"))
print(is_matched_alt_1_1("{)[](}]}]}))}(())("))
            
#print(is_matched_alt_1_1("{[()]}"))
#print(is_matched_alt_1_1("{[(])}"))
#print(is_matched_alt_1_1("{{[[(())]]}}"))

#print(is_matched_alt_1_1("()[{}()]([[][]()[[]]]{()})([]()){[]{}}{{}}{}(){([[{}([]{})]])}"))
#print(is_matched_alt_1_1("{][({(}]][[[{}]][[[())}[)(]([[[)][[))[}[]][()}))](]){}}})}[{]{}{((}]}{{)[{[){{)[]]}))]()]})))["))
#print(is_matched_alt_1_1("[)](][[([]))[)"))
#print(is_matched_alt_1_1("]}]){[{{){"))
#print(is_matched_alt_1_1("{[(}{)]]){(}}(][{{)]{[(((}{}{)}[({[}[}((}{()}[]})]}]]))((]][[{{}[(}})[){()}}{(}{{({{}[[]})]{((]{[){["))
#print(is_matched_alt_1_1("()}}[(}])][{]{()([}[}{}[{[]{]](]][[))(()[}(}{[{}[[]([{](]{}{[){()[{[{}}{[{()(()({}([[}[}[{(]})"))
#print(is_matched_alt_1_1("){[])[](){[)}[)]}]]){](]()]({{)(]])(]{(}(}{)}])){[{}((){[({(()[[}](]})]}({)}{)]{{{"))
#print(is_matched_alt_1_1("[(})])}{}}]{({[]]]))]})]"))
#print(is_matched_alt_1_1("[{"))
#print(is_matched_alt_1_1("{}([{()[]{{}}}])({})"))
#print(is_matched_alt_1_1("{({}{[({({})([[]])}({}))({})]})}"))
#print(is_matched_alt_1_1("()[]"))
#print(is_matched_alt_1_1("{)[])}]){){]}[(({[)[{{[((]{()[]}][([(]}{](])()(}{(]}{})[)))[](){({)][}()(("))
#print(is_matched_alt_1_1("[][(([{}])){}]{}[()]{([[{[()]({}[])()()}[{}][]]])}"))
#print(is_matched_alt_1_1("(}]}"))
#print(is_matched_alt_1_1("(([{()}]))[({[{}{}[]]{}})]{((){}{()}){{}}}{}{{[{[][]([])}[()({}())()({[]}{{[[]]([])}})()]]}}"))
#print(is_matched_alt_1_1("[(([){[](}){){]]}{}([](([[)}[)})[(()[]){})}}]][({[}])}{(({}}{{{{])({]]}[[{{(}}][{)([)]}}"))
#print(is_matched_alt_1_1("()()[()([{[()][]{}(){()({[]}[(((){(())}))]()){}}}])]"))
#print(is_matched_alt_1_1("({)}]}[}]{({))}{)]()(](])})][(]{}{({{}[]{][)){}{}))]()}((][{]{]{][{}[)}}{)()][{[{{[["))
#print(is_matched_alt_1_1(")}(()[])(}]{{{}[)([})]()}()]}(][}{){}}})}({](){([()({{(){{"))
#print(is_matched_alt_1_1("}([]]][[){}}[[)}[(}(}]{(}[{}][{}](}]}))]{][[}(({(]}[]{[{){{(}}[){[][{[]{[}}[)]}}]{}}(}"))
#
#lefts = '{[('
#rights = '}])'
#closes = { a:b for a,b in zip(rights,lefts)}
#print(closes)

"""QUEUE - FIFO """

class Queue:
    def __init__(self):
        self.__top = -1
        self.__data_store = Stack()
        self.__dequeue_helper_data_store = Stack()
        self.__peekCandidate = None
    
    def enqueue(self,element):
        self.__peekCandidate = element
        self.__data_store.push(element)
    
    def dequeue(self):
       
        current_pop = None
        
        print(self.__data_store.isEmpty())
        
        while (self.__data_store.isEmpty() == False):
            if self.__data_store.count() == 1:
                return self.__data_store.pop()
            else:
                while not self.__data_store.isEmpty():
                    current_pop = self.__data_store.pop()
                    self.__dequeue_helper_data_store.push(current_pop)
                    
                    #print("__data_store AFTER POP %s" %(self.__data_store._data_store))
                    #print("__data_store count %s" %(self.__data_store.count()))
                    
                    #first element
                    if self.__data_store.count() == 1:
                        #print("__data_store AFTER POP at count == 1 %s" %(self.__data_store._data_store))
                        current_pop = self.__data_store.pop()
                        #print("__data_store AFTER  final POP %s" %(self.__data_store._data_store))
                        
        while not self.__dequeue_helper_data_store.isEmpty():
            popped_value  = self.__dequeue_helper_data_store.pop()
            print("popped %s" %(popped_value))
            self.__data_store.push(popped_value)
            print("__data_store %s" %(self.__data_store._data_store))
                        
        return current_pop
    
    def isEmpty(self):
        return self.__data_store.isEmpty()
    
    def peek(self):
        return self.__peekCandidate
    
    def show_all(self):
        while not self.__data_store.isEmpty():
            current_pop = self.__data_store.pop()
            self.__dequeue_helper_data_store.push(current_pop)
                
            
queue = Queue()
for element in range(0,6):
    print(queue._Queue__peekCandidate)
    queue.enqueue(element)

print("peek")
print(queue._Queue__peekCandidate)

print(queue._Queue__data_store._data_store)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

queue.enqueue(9)

print_on_demand(True,queue._Queue__data_store._data_store)
print(queue._Queue__data_store._data_store)
 