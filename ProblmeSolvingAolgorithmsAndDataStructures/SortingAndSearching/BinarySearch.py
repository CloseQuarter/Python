# =============================================================================
# # -*- coding: utf-8 -*-
# """
# Created on Mon Apr  2 00:05:30 2018
# 
# @author: sanooj
# """
# 
# def binary_search_my_attempt(a_list, item):
#     
#     pos = 0
#     found = False
#     list_count = len(a_list)
#     
#     partial_array = a_list[:]
#     partial_array_count = \
#     list_count
#     
#     #length = 1 
#     if partial_array_count == 1:
#         
#         if partial_array[0] == item:
#             return True
#         
#         else:
#             return False
#         
#     
#     while not partial_array_count // 2 == 0 and not found:
#         
#         #partition
#         if partial_array[partial_array_count // 2] >= item:
#             partial_array = \
#             partial_array[:((partial_array_count // 2) + 1)]
#             
#             partial_array_count = \
#             len(partial_array)
#         
#         else:
#             partial_array = \
#             partial_array[(partial_array_count // 2):]
#             
#             partial_array_count = \
#             len(partial_array)
#     
#         
#         if partial_array_count // 2 == 0:
#             if partial_array[0] == item:
#                 found = True
#     
# # =============================================================================
# #         while pos < partial_array_count and not found:
# #             
# #             if partial_array[pos] == item:
# #                 found = True
# #             
# #             else:
# #                 pos = pos+1
# #                 
# #             
# #         pos = 0          
# # =============================================================================
#             
# 
#     return found
# 
# array = [1,2,3,4,5,6]
# 
# #array = [0,3]
# 
# #mid element
# print(binary_search_my_attempt(array, 3))
# 
# #end
# #print(binary_sbinary_search_my_attemptearch(array, 5))
# 
# #first
# #print(binary_search_my_attempt(array, 1))
# 
# #none
# #print(binary_sebinary_search_my_attemptarch(array, 15))
# 
# 
# 
# 
# =============================================================================

def binary_search(a_list, item):
    
    first = 0
    last = len(a_list) - 1
    
    found = False
    
    while first <= last and not found:
        
        midpoint = (first + last) // 2
        print("first %d" %(first))
        print("last %d" %(last))
        print("midpoint %d" %(midpoint))
        
        if a_list[midpoint] == item:
            found = True
            
        else:
            
            if item < a_list[midpoint]:
                last = midpoint - 1
            
            else:
                first = midpoint + 1
        
    return found
    

array = [1,2,3,4,5,6]
 
#array = [0,3]
 
#mid element
#print(binary_search(array, 3))
 
#end
#print(binary_search(array, array[(len(array) - 1)]))
 
#first
#print(binary_search(array, array[0]))
 
#none
print(binary_search(array, 15))           