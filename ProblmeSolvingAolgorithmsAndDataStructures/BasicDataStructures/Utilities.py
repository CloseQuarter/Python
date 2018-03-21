# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 18:29:37 2018

@author: sanooj
"""

DEBUG = True

def debug_print(print_func=print):
    
    def debug_print(f_arg, *argv,flag:bool=DEBUG) -> None:
        if flag == True:
            if len(argv) >= 2:
                for arg in argv:
                    print_func(arg)
            else:
                print_func(f_arg)
        else:
            pass

    return debug_print
    
debug_print("ball %s" %("apple"))


def debug_print1(f_arg, *argv) -> None:
        if f_arg != None:
            if len(argv) >= 0:
                for arg in argv:
                    print(arg.strip(","))
                    f_arg(arg.strip(","))
            else:
                pass
        else:
            pass
        
debug_print1(print,"ball %s" %("apple"))

def print_on_demand(did_demand=DEBUG,*argv):
    
    if not DEBUG:
        return
    
    if len(argv) == 0:
        print(did_demand)
    elif did_demand:
        if len(argv) > 0:
            print(argv[0])
        else:
            print(argv)
        
#print_on_demand(False,"ball")
print_on_demand(True,"ball %s" %("capple"))
print_on_demand("ball %s" %("dcapple"))