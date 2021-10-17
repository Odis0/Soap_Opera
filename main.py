
import enum
import random
from entity import Entity
from room import Room
from worldModule import WorldModule
from world import World



world1 = World()
world1.WorldSetup()
#print(world1.GetWorldModule3DArray()[2][4][1].GetModuleRoom().GetRoomName())
#print(world1.CheckClassWorldModule(world1.GetWorldModule3DArray()[2][4][1]))
#print(world1.GetWorldModule3DArray()[2][4][1])
print(world1.GetWorldModuleFrom3DArray(world1.GetWorldModuleLocationDictionary()[0]))
print(world1.GetWorldModuleLocationDictionary()[0])
print(world1.GetWorldModuleFrom3DArray((1,2,0)).GetModuleRoom().GetRoomName())