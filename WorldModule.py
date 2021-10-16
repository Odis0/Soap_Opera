class WorldModule:
    def __init__(self, room, xAxis, yAxis, zAxis):
        self.__room = room
        self.__xAxis = xAxis
        self.__yAxis = yAxis
        self.__zAxis = zAxis

    def GetModuleRoom(self):
        return self.__room

    def GetXAxis(self):
        return self.__xAxis

    def GetYAxis(self):
        return self.__yAxis

    def GetZAxis(self):
        return self.__zAxis