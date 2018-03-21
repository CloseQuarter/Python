# -*- coding: utf-8 -*-
"""
Created on Tue Mar  6 22:17:19 2018

@author: sanooj
"""

"""
Hot Potato game simulation

1. pass potato around for a fixed number of times "t" amongst
    a fixed number of people "p"
2. person in possession when the count of hands exchanged is "t"
    is eliminated
3. game resumes with the person who was previously adjacent to the 
    person eliminated
"""

from DataStructures.Queue import Queue

def hot_potato(name_list, num):
    
    #number_of_rounds
    number_of_rounds = num
    
    #empty queue
    sim_queue = Queue()
    
    #populate the Queue
    for name in name_list:
        sim_queue.enqueue(name)
        
    print(sim_queue.items)
    
    #game end when Queue.size == 1
    while sim_queue.size() > 1:
        
        #loop till the number_of_rounds limit 
        for index in range(number_of_rounds):
            
            #going in a circle
            #simulating passing the ball
            #imagine children moving through a pipe
            # exiting from front
            # and reentering through the rear
            # until the number of exits = limit
            # eliminate the kid who is at the front end
            #dequeing and enqueing
            #dequeue
            name = sim_queue.dequeue()
            
            #enque it back as we have to go more rounds
            sim_queue.enqueue(name)
        
        #one round complete
        #deque that person
        sim_queue.dequeue()
    
    print(sim_queue.items)
     
    return sim_queue.dequeue()
        
 
    

print(hot_potato(["Bill", "David", "Susan", "Jane", "Kent",
"Brad"], 7)) 



















       