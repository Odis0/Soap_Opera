class Room:
    def __init__(self, roomName):
        #self.__roomID = roomID
        self.__roomName = roomName
        #self.__roomCoordinates = (xAxis, yAxis, zAxis)  #All entities should have a coordinate, but they pass it up to director, which will then tell them what else is in the room. Inventory should be enums, delete the object when it goes in inventory. You just create an instance of the object from inventory when you need it.
        # self.__connectionList = connectionList
#        self.__roomInventory = roomInventory

    def GetRoomName(self):
        return self.__roomName
