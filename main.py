
import enum
import random
from Entity import Entity
from Room import Room
from WorldModule import WorldModule

class RoomID():
    Basement = 0
    Front_Yard = 1
    Office = 2
    Entry_Hall = 3
    Garage = 4
    Kitchen = 5
    Daughter_Room = 6
    Living_Room = 7
    Down_Bathroom = 8
    Back_Patio = 9
    Pool = 10
    Closet = 11
    Mast_Bathroom = 12
    Mast_Bedroom = 13
    Son_Room = 14
    Landing = 15
    Studio = 16

class EntityID():
    Ethan = 0


class World:
    def __init__(self):
        self.__worldModule3DArray = [[[[] for i in range(5)] for j in range(5)] for k in range(5)]
        self.__roomTuplesList = [
        ("Basement", (1, 2, 0)),
        ("Front_Yard", (0, 1, 1)),
        ("Office", (0, 1, 1)),
        ("Entry_Hall", (1, 1, 1)),
        ("Garage", (2, 1, 1)),
        ("Kitchen", (1, 2, 1)),
        ("Daughter_Room", (0, 3, 1)),
        ("Living_Room", (1, 3, 1)),
        ("Down_Bathroom", (2, 3, 1)),
        ("Back_Patio", (1, 4, 1)),
        ("Pool", (2, 4, 1)),
        ("Closet", (1, 0, 2)),
        ("Mast_Bathroom", (0, 1, 2)),
        ("Mast_Bedroom", (1, 1, 2)),
        ("Son_Room", (0, 2, 2)),
        ("Landing", (1, 2, 2)),
        ("Studio", (1, 3, 2))
                            ]

    def GetRoomTuplesList(self):
        return self.__roomTuplesList

    def GetRoomNameFromTuple(self, roomTuple):
        return roomTuple[0]

    def GetRoomCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[1]

    def GetXAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[0]

    def GetYAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[1]

    def GetZAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[2]

    def InitializeRoom(self, roomName):
        initializedRoom = Room(roomName)
        return initializedRoom

    def InitializeAllRooms(self):
        initializedRoomList = []
        for roomTuple in self.GetRoomTuplesList():
            initializedRoom = Room(self.GetRoomNameFromTuple(roomTuple))
            initializedRoomList.append(initializedRoom)
        return initializedRoomList

    def InitializeWorldModule(self, roomModule, coordinateTuple):
        initializedModule = WorldModule(roomModule,self.GetXAxisFromCoordinateTuple(coordinateTuple), self.GetYAxisFromCoordinateTuple(coordinateTuple), self.GetZAxisFromCoordinateTuple(coordinateTuple))
        return initializedModule


    def InitializeAllWorldModules(self):
        initializedRoomList = self.InitializeAllRooms()
        initializedWorldModuleList = []
        for initializedRoom, roomTuple in enumerate(self.GetRoomTuplesList()):
            initializedWorldModule = self.InitializeWorldModule(initializedRoomList[initializedRoom], self.GetRoomCoordinateTuple(roomTuple))
            initializedWorldModuleList.append(initializedWorldModule)
        return initializedWorldModuleList

    def SetWorldModule3DArrayLocation(self, initializedWorldModuleList):
        for worldModule in initializedWorldModuleList:
            self.__worldModule3DArray[worldModule.GetXAxis()][worldModule.GetYAxis()][worldModule.GetZAxis()].append(worldModule)

    def GetWorldModule3DArray(self):
        return self.__worldModule3DArray

    def WorldSetup(self):
        initializedWorldModuleList = self.InitializeAllWorldModules()
        self.SetWorldModule3DArrayLocation(initializedWorldModuleList)

#To  this point are all WorldSetup Functions

    def CheckClassWorldModule(self, worldModule):
        return isinstance(worldModule,WorldModule)


    def GetWorldModuleFrom3DArray(self, xAxis, yAxis, zAxis):
        for initializedObject in self.__worldModule3DArray[xAxis][yAxis][zAxis]:
            if self.CheckClassWorldModule(initializedObject):
                return initializedObject







world1 = World()
world1.WorldSetup()
#print(world1.GetWorldModule3DArray()[2][4][1].GetModuleRoom().GetRoomName())
print(world1.CheckClassWorldModule(world1.GetWorldModule3DArray()[2][4][1]))
print(world1.GetWorldModule3DArray()[2][4][1])
print(world1.GetWorldModuleFrom3DArray(4,4,1))

