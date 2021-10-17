from worldModule import WorldModule
from room import Room

class World:
    def __init__(self):
        self.__worldModule3DArray = [[[[] for i in range(5)] for j in range(5)] for k in range(5)]
        self.__worldModuleLocationList = [None for i in range(100)]

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

    def SetModuleCoordinateInLocationDictionary(self, worldModuleKey, coordinateTuple):
        self.__worldModuleLocationList[worldModuleKey] = coordinateTuple


    def InitializeAllWorldModules(self):
        initializedRoomList = self.InitializeAllRooms()
        initializedWorldModuleList = []
        for initializedRoom, roomTuple in enumerate(self.GetRoomTuplesList()):
            initializedWorldModule = self.InitializeWorldModule(initializedRoomList[initializedRoom], self.GetRoomCoordinateTuple(roomTuple))
            initializedWorldModuleList.append(initializedWorldModule)
        return initializedWorldModuleList

    def SetWorldModule3DArrayLocation(self, initializedWorldModuleList):
        for counter, worldModule in enumerate(initializedWorldModuleList):
            self.SetModuleCoordinateInLocationDictionary(counter, worldModule.GetCoordinateTuple())
            self.__worldModule3DArray[worldModule.GetXAxis()][worldModule.GetYAxis()][worldModule.GetZAxis()].append(worldModule)


    def GetWorldModuleLocationDictionary(self):
        return self.__worldModuleLocationList


    def GetWorldModule3DArray(self):
        return self.__worldModule3DArray

    def WorldSetup(self):
        initializedWorldModuleList = self.InitializeAllWorldModules()
        self.SetWorldModule3DArrayLocation(initializedWorldModuleList)


    def CheckClassWorldModule(self, worldModule):
        return isinstance(worldModule,WorldModule)


    def GetWorldModuleFrom3DArray(self, coordinateTuple):
        for initializedObject in self.__worldModule3DArray[self.GetXAxisFromCoordinateTuple(coordinateTuple)][self.GetYAxisFromCoordinateTuple(coordinateTuple)][self.GetZAxisFromCoordinateTuple(coordinateTuple)]:
            if self.CheckClassWorldModule(initializedObject):
                return initializedObject


    def CalculateWorldModuleXAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetXAxis() - worldModule1.GetXAxis())

    def CalculateWorldModuleYAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetYAxis() - worldModule1.GetYAxis())

    def CalculateWorldModuleZAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetZAxis() - worldModule1.GetZAxis())

    def CalculateWorldModuleTotalDistance(self, worldModule1, worldModule2):
        xDistance = self.CalculateWorldModuleXAxisDistance(worldModule1, worldModule2)
        yDistance = self.CalculateWorldModuleYAxisDistance(worldModule1, worldModule2)
        zDistance = self.CalculateWorldModuleZAxisDistance(worldModule1,worldModule2)
        totalDistance = xDistance + yDistance + zDistance
        return totalDistance

    #def CheckWorldModuleAdjacencyInArray(self,worldModule1, worldModule2):
