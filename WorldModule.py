class WorldModule:
    def __init__(self, room, xAxis, yAxis, zAxis): #Change room to module object. Static objects.
        self.__room = room
        self.__coordinateTuple = (xAxis, yAxis, zAxis)

    def GetModuleRoom(self):
        return self.__room

    def GetXAxis(self):
        return self.__coordinateTuple[0]

    def GetYAxis(self):
        return self.__coordinateTuple[1]

    def GetZAxis(self):
        return self.__coordinateTuple[2]

    def GetCoordinateTuple(self):
        return self.__coordinateTuple