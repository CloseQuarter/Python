# -*- coding: utf-8 -*-
"""
Created on Fri May 25 18:05:40 2018

@author: sanooj
"""

#---------------------------
#     Provide an interface for 
#    creating families of related or dependent objects 
#    without specifying their concrete classes   
#
#------------------------------
"""

Abstract factory                                                    <--- Client
 - CreateProductA()                                 
 - CreateProductB()                                            Abstract ProductA
       |
       |                                                               |
     -------------------                                      --------------------
     |                 |                                      |                   |
                                                     |----> ProductA2            ProductA1  
ConcreteFactory1      ConcreteFactory2               |
 -- CreateProductA()     -- CreateProductA()  -------|   
 -- CreateProductB()     -- CreateProductB()         |          Abstract ProductB
                                                     |                 |
                                                     |       -------------------
                                                     |-------|                  |
                                                             ProductB2          ProductB2
                                                             







"""                             

class Direction:
    North = "North"
    South = "South"
    East  = "East"
    West  = "West"
    
class MapSite:
    def Enter(self):
        pass
    
class Room(MapSite):
    
    def __init__(self,roomNumber):
        self._roomNumber = roomNumber
        self._sides = []
        
    def GetSide(self,direction:Direction):
        pass
    
    def SetSide(self,direction:Direction, mapSite:MapSite):
        pass
    
    #from MapSite
    def Enter(self):
        super.Enter()
        
class Wall(MapSite):
    
    def __init__(self):
        pass
    
    #from MapSite
    def Enter(self):
        super.Enter()
        
        
class Door(MapSite):
    
    def __init__(self, room1:Room = None, room2:Room = None):
        self._room1 = room1
        self._room2 = room2
        self._isOpen = False
        pass
    
    #from MapSite
    def Enter(self):
        super.Enter()
        
    def OtherSideFrom(room:Room) -> Room:
        return None
    
class Maze:
    
    def __init__(self):
        pass
    
    def AddRoom(self,room:Room):
        pass
    
    def RoomNo(self, roomNumber:int) -> Room:
        return None
    
    
        
    
       
    