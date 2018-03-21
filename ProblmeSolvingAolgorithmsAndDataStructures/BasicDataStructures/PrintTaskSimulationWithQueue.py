# -*- coding: utf-8 -*-
"""
Created on Fri Mar  9 20:00:00 2018

@author: sanooj
"""

"""
Print Queue simulaton

Here is the main simulation.
1. Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The
queue is empty to start.

2. For each second (current_second):
• Does a new print task get created? If so, add it to the queue with the current_second
as the timestamp.
• If the printer is not busy and if a task is waiting,
– Remove the next task from the print queue and assign it to the printer.
– Subtract the timestamp from the current_second to compute the waiting time
for that task.
– Append the waiting time for that task to a list for later processing.
– Based on the number of pages in the print task, figure out how much time will
be required.
• The printer now does one second of printing if necessary. It also subtracts one
second from the time required for that task.
• If the task has been completed, in other words the time required has reached zero,
the printer is no longer busy.
3. After the simulation is complete, compute the average waiting time from the list of waiting
times generated.

"""


import random
import Utilities


"""
Assumptions

time students get to use printer = 
1hr a day 

No. of Students = 
10

page length = 
1-20
"""


# represents a single print task
#-> keeps a time created time stamp
#-> holds number of pages
#--> computes wait time  
class Task:
    
    def __init__(self, time):
        self.time_stamp = time
        self.pages = \
        random.randrange(1,21)
        
    def get_stamp(self):
        return self.time_stamp
    
    def get_pages(self):
        return self.pages
    
    def wait_time(self, current_time):
        return current_time - self.time_stamp
    
    

class Printer:
    
    def __init__(self, ppm:int):
        #pages per minute
        self.page_rate = ppm
        
        #current task
        self.current_task = None
        
        #internal timer
        self.time_remaining = 0
        
        
    """
    decrements the internal timer and 
    sets the printer to idle if the task is completed.
    """
    def tick(self):
        
        #check if printer is executing a task
        if self.current_task != None:
            
            #if Yes
            #decrement the timer
            self.time_remaining = self.time_remaining - 1
            
            #check if timer is 0 or less 
            if self.time_remaining <= 0:
                
                #if YES
                #set printer idle
                #i.e finish the task
                self.current_task = None
                
    
    def busy(self) -> bool:
        if self.current_task != None:
            return True
        else:
            return False
    
    def start_next(self,new_task):
        
        #set current_task
        self.current_task = new_task
       
        #time required to complete the task
        # page_rate =  number_of_pages / time
        #  .
        # . . time = number_of_pages / rate
        page_rate_in_hours = self.page_rate / 60 
        self.time_remaining = (
                new_task.get_pages() / page_rate_in_hours
                ) 
        
        
from DataStructures.Queue import Queue

"""
# for 10 students 
# printing 2 times
# 2 * 10 tasks/hr
# (2 * 10) / 60 tasks/min
# (2 * 10) / (60 * 60) tasks/sec = 20 / 3600 = 1 / 180
# 1 task per 180 mins
"""
# a task arrives 1 every 180 sec
def new_print_task() -> bool:
    
    num = random.randrange(1,181)
    
    if num == 180:
        Utilities.print_on_demand(
                False,
                "new_print_task %s" %(num)
                )
        return True
    else:
        return False

def simulation(
        num_seconds:int, 
        pages_per_minute:int):
    
    lab_printer = Printer(
            pages_per_minute
            )
    
    print_queue = Queue()
    
    waiting_times = []
    
    #loop through each second
    for current_second in range(num_seconds):
        
        #check if a print task has been created
        ## the code to check that
        ## generates a print task every 180 sec
        if new_print_task():
            
            #print task created
            task = Task(current_second)
            
            #enqueue the atsk
            print_queue.enqueue(task)
        
        #check printer status
        # check if printer is busy
        # Check if print_queue is empty
        if ((not lab_printer.busy()) and 
           (not print_queue.is_empty())):
            
            #printer is idle and tasks in queue
            
            #get next task from qeueue
            next_task = print_queue.dequeue()
            
            #calculate wait time i.e 
            # current_time - task_created_time_stamp
            wait_time = next_task.wait_time(
                    current_second
                    )
            
            #add to list to calculate average wait time
            waiting_times.append(wait_time)
                    
            #start task
            # The printer now does one second of printing
            # also subtracts 1 second 
            # from the time required for that task.
            lab_printer.start_next(next_task)
              
        #manage printer state
        # if no task ..set to idle
        lab_printer.tick()
    
    #calculate average wait time    
    average_wait = \
    sum( waiting_times ) / len(waiting_times)
    print(
            "Average Wait %6.2f secs %3d tasks remaining." \
            %(average_wait, print_queue.size())
            )
    
Utilities.print_on_demand("***5***")
for i in range(10):
    simulation(3600,5)

Utilities.print_on_demand("***10***")

for i in range(10):
    simulation(3600,10)



            