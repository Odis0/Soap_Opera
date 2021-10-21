from worldModule import WorldModule
from room import Room
from entity import Entity
from agent import Agent

class World:
    def __init__(self):
        self.__worldModule3DArray = [[[[] for i in range(5)] for j in range(5)] for k in range(5)]
        self.__worldModuleLocationList = [None for i in range(1000)]
        self.__entityLocationList = [None for i in range(1000)]

        self.__roomTuplesList = [
        ("Basement", (1, 2, 0)),
        ("Front_Yard", (1, 0, 1)),
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
        self.__entityTuplesList = [
            ("Aaron",(1,1,1),Agent),
            ("Wheelbarrow", (0, 2, 2), Entity)
        ]



    def GetRoomTuplesList(self):
        return self.__roomTuplesList

    def GetRoomNameFromTuple(self, roomTuple):
        return roomTuple[0]

    def GetCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[1]

    def GetXAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[0]

    def GetYAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[1]

    def GetZAxisFromCoordinateTuple(self, coordinateTuple):
        return coordinateTuple[2]

    def GetEntityTuplesList(self):
        return self.__entityTuplesList

    def GetEntityNameFromTuple(self, entityTuple):
        return entityTuple[0]

    def GetEntityTypeFromTuple(self, entityTuple):
        return entityTuple[2]

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



    def SetModuleCoordinateInLocationList(self, worldModuleID, coordinateTuple):
        self.__worldModuleLocationList[worldModuleID] = coordinateTuple


    def InitializeAllWorldModules(self):
        initializedRoomList = self.InitializeAllRooms()
        initializedWorldModuleList = []
        for initializedRoom, roomTuple in enumerate(self.GetRoomTuplesList()):
            initializedWorldModule = self.InitializeWorldModule(initializedRoomList[initializedRoom], self.GetCoordinateTuple(roomTuple))
            initializedWorldModuleList.append(initializedWorldModule)
        return initializedWorldModuleList



    def SetAllObjectIDs(self, initializedObjectsList):
        for counter, initializedObject in enumerate(initializedObjectsList):
            initializedObject.SetID(counter)


    def SetWorldModule3DArrayLocation(self, initializedWorldModuleList):
        self.SetAllObjectIDs(initializedWorldModuleList)
        for worldModule in initializedWorldModuleList:
            self.SetModuleCoordinateInLocationList(worldModule.GetWorldModuleID(), worldModule.GetCoordinateTuple())
            self.__worldModule3DArray[worldModule.GetXAxis()][worldModule.GetYAxis()][worldModule.GetZAxis()].append(worldModule)




    def InitializeAllEntities(self):
        initializedEntityList = []
        for entityTuple in self.GetEntityTuplesList():
            entityType = self.GetEntityTypeFromTuple(entityTuple)
            initializedEntity = entityType(self.GetEntityNameFromTuple(entityTuple))
            initializedEntityList.append(initializedEntity)
        return initializedEntityList

    def SetEntityCoordinateInLocationList(self, entityID, coordinateTuple):
        self.__entityLocationList[entityID] = coordinateTuple

    def SetEntity3DArrayLocation(self, initializedEntityList):
        self.SetAllObjectIDs(initializedEntityList)
        for counter, entity in enumerate(initializedEntityList):
            entityCoordinateTuple = self.GetCoordinateTuple(self.GetEntityTuplesList()[counter])
            self.SetEntityCoordinateInLocationList(entity.GetEntityID(), entityCoordinateTuple)
            self.__worldModule3DArray[self.GetXAxisFromCoordinateTuple(entityCoordinateTuple)][self.GetYAxisFromCoordinateTuple(entityCoordinateTuple)][self.GetZAxisFromCoordinateTuple(entityCoordinateTuple)].append(entity)



    def WorldSetup(self):
        initializedWorldModuleList = self.InitializeAllWorldModules()
        self.SetWorldModule3DArrayLocation(initializedWorldModuleList)
        initializedEntityList = self.InitializeAllEntities()
        self.SetEntity3DArrayLocation(initializedEntityList)


    def CheckClassWorldModule(self, worldModule):
        return isinstance(worldModule,WorldModule)


    def GetWorldModuleLocationList(self):
        return self.__worldModuleLocationList


    def GetWorldModule3DArray(self):
        return self.__worldModule3DArray

    def GetAllObjectsAt3DArrayLocation(self, coordinateTuple):
        return self.__worldModule3DArray[self.GetXAxisFromCoordinateTuple(coordinateTuple)][self.GetYAxisFromCoordinateTuple(coordinateTuple)][self.GetZAxisFromCoordinateTuple(coordinateTuple)]

    def GetWorldModuleFrom3DArray(self, coordinateTuple):
        try:
            for initializedObject in self.GetAllObjectsAt3DArrayLocation(coordinateTuple):
                if self.CheckClassWorldModule(initializedObject):
                    return initializedObject
        except:
            pass


    def CalculateWorldModuleXAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetXAxis() - worldModule1.GetXAxis())

    def CalculateWorldModuleYAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetYAxis() - worldModule1.GetYAxis())

    def CalculateWorldModuleZAxisDistance(self, worldModule1, worldModule2):
        return abs(worldModule2.GetZAxis() - worldModule1.GetZAxis())

    def CalculateWorldModuleTotalDistance(self, worldModule1, worldModule2):
        try:
            xDistance = self.CalculateWorldModuleXAxisDistance(worldModule1, worldModule2)
            yDistance = self.CalculateWorldModuleYAxisDistance(worldModule1, worldModule2)
            zDistance = self.CalculateWorldModuleZAxisDistance(worldModule1,worldModule2)
            totalDistance = xDistance + yDistance + zDistance
            return totalDistance
        except:
            pass


    def CheckWorldModuleCoordinateAdjacency(self,worldModule1, worldModule2):
        return self.CalculateWorldModuleTotalDistance(worldModule1,worldModule2) == 1

    def GetEntityLocationList(self):
        return self.__entityLocationList

    def GetEntityCoordinateTuple(self, entityID):
        return self.GetEntityLocationList()[entityID]

