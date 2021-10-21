
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
#print(world1.GetWorldModuleFrom3DArray(world1.GetWorldModuleLocationDictionary()[0]))
#print(world1.GetWorldModuleLocationDictionary()[0])
#print(world1.GetWorldModuleFrom3DArray((1,2,0)).GetModuleRoom().GetRoomName())
print(world1.CalculateWorldModuleTotalDistance(world1.GetWorldModuleFrom3DArray((2,4,1)),world1.GetWorldModuleFrom3DArray((0,1,1))))
print(world1.CheckWorldModuleCoordinateAdjacency(world1.GetWorldModuleFrom3DArray((1,0,1)),world1.GetWorldModuleFrom3DArray((4,1,1))))
print(world1.GetWorldModuleFrom3DArray((4,4,4)))
print(world1.GetAllObjectsAt3DArrayLocation((1,1,1)))
print(world1.GetEntityCoordinateTuple(1))