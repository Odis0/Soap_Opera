
import enum
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


class Room:
    def __init__(self, roomName, xAxis, yAxis, zAxis, connectionList, roomInventory = []):
        self.__roomName = roomName
        self.__roomCoordinates = (xAxis, yAxis, zAxis)
        self.__connectionList = connectionList
        self.__roomInventory = roomInventory

    def GetRoomConnections(self):
        return self.__connectionList

    def GetRoomInventory(self):
        return self.__roomInventory

    def SetRoomInventory(self, targetEntity):
        self.__roomInventory.append(targetEntity)

    def RemoveRoomInventory(self,targetEntity):
        self.__roomInventory.remove(targetEntity)

    def GetRoomName(self):
        return self.__roomName


class Entity:
    def __init__(self, entityName, entityRoom):
        self.__entityName = entityName
        self.__entityRoom = entityRoom

    def GetEntityRoom(self):
        return self.__entityRoom

    def GetEntityName(self):
        return self.__entityName


def EntityMove(targetEntity,targetDestination):
    roomList[targetDestination].SetRoomInventory(targetEntity)
    roomList[targetEntity.GetEntityRoom()].RemoveRoomInventory(targetEntity)
    print(f"{targetEntity.GetEntityName()} moved from {roomList[targetEntity.GetEntityRoom()].GetRoomName()} to {roomList[targetDestination].GetRoomName()}.")






entityList = [Entity("Ethan",RoomID.Kitchen)
]


roomList = [Room("Basement", 1 , 2, 0, connectionList=[RoomID.Kitchen]),
            Room("Front Yard", 0 , 1, 1, connectionList=[RoomID.Entry_Hall]),
            Room("Office", 0, 1, 1, connectionList=[RoomID.Entry_Hall]),
            Room("Entry Hall", 1, 1, 1, connectionList=[RoomID.Office,RoomID.Garage,RoomID.Kitchen]),
            Room("Garage", 2, 1, 1, connectionList=[RoomID.Entry_Hall]),
            Room("Kitchen", 1, 2, 1, connectionList=[RoomID.Entry_Hall,RoomID.Living_Room,RoomID.Basement,RoomID.Landing],roomInventory=[entityList[EntityID.Ethan]]),
            Room("Daughter's Room", 0,3,1,connectionList=[RoomID.Living_Room]),
            Room("Living Room",1,3,1, connectionList=[RoomID.Daughter_Room,RoomID.Kitchen,RoomID.Back_Patio,RoomID.Down_Bathroom]),
            Room("Downstairs Bathroom",2,3,1, connectionList=[RoomID.Living_Room]),
            Room("Backyard Patio",1,4,1, connectionList=[RoomID.Living_Room,RoomID.Pool]),
            Room("Pool",2,4,1, connectionList=[RoomID.Back_Patio]),
            Room("Walk-in Closet",1,0,2, connectionList=[RoomID.Mast_Bedroom]),
            Room("Master Bathroom",0,1,2, connectionList=[RoomID.Mast_Bedroom]),
            Room("Master Bedroom",1,1,2, connectionList=[RoomID.Mast_Bathroom,RoomID.Closet,RoomID.Landing]),
            Room("Son's Room",0,2,2, connectionList=[RoomID.Landing]),
            Room("Upper Landing", 1,2,2, connectionList=[RoomID.Kitchen,RoomID.Mast_Bedroom,RoomID.Son_Room,RoomID.Studio]),
            Room("Art Studio",1,3,2, connectionList=[RoomID.Landing])
            ]

print(roomList[RoomID.Kitchen].GetRoomConnections())
print(roomList[RoomID.Entry_Hall].GetRoomInventory())
print(roomList[RoomID.Kitchen].GetRoomInventory())
EntityMove(entityList[EntityID.Ethan],RoomID.Entry_Hall)
print(roomList[RoomID.Entry_Hall].GetRoomInventory())