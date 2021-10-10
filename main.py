
import enum
import random


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
    def __init__(self, roomID, roomName, xAxis, yAxis, zAxis, connectionList, roomInventory = []):
        self.__roomID = roomID
        self.__roomName = roomName
        self.__roomCoordinates = (xAxis, yAxis, zAxis)  #All entities should have a coordinate, but they pass it up to director, which will then tell them what else is in the room. Inventory should be enums, delete the object when it goes in inventory. You just create an instance of the object from inventory when you need it.
        self.__connectionList = connectionList
        self.__roomInventory = roomInventory

    def GetRoomConnections(self):
        return self.__connectionList

    def GetRoomInventory(self):
        return self.__roomInventory

    def AddRoomInventory(self, targetEntity):
        self.__roomInventory.append(targetEntity)

    def RemoveRoomInventory(self,targetEntity):
        self.__roomInventory.remove(targetEntity)

    def GetRoomName(self):
        return self.__roomName

    def GetRoomID(self):
        return self.__roomID


class Entity:
    def __init__(self, entityName, entityRoom):
        self.__entityName = entityName
        self.__entityRoom = entityRoom

    def GetEntityRoom(self):
        return self.__entityRoom

    def GetEntityName(self):
        return self.__entityName

    def SetEntityRoom(self, targetDestination):
        self.__entityRoom = targetDestination


def EntityMove(targetEntity,targetDestination):   #Pass in the objects themselves.
    startRoom = targetEntity.GetEntityRoom()
    targetDestination.AddRoomInventory(targetEntity)
    roomList[startRoom].RemoveRoomInventory(targetEntity)
    targetEntity.SetEntityRoom(targetDestination.GetRoomID())
    print(f"{targetEntity.GetEntityName()} moved from {roomList[startRoom].GetRoomName()} to {targetDestination.GetRoomName()}.")

def GetEntityRoom(targetEntity):
    return roomList[targetEntity.GetEntityRoom()]

def GetEntityRoomName(targetEntity):
    return GetEntityRoom(targetEntity).GetRoomName()


Ethan = Entity("Ethan",RoomID.Kitchen)

entityList = [Ethan]

Basement =          Room(0, "Basement", 1 , 2, 0, connectionList=[RoomID.Kitchen])  #Static objects should be held by the room, but MOVEABLE objects should be independent. XYZ of player should be linked up with the XYZ of the room by the director. OR have a world object that curates lists and passes it to the director. If two things interact, a higher thing should mediate them.
Front_Yard =        Room(1, "Front Yard", 0 , 1, 1, connectionList=[RoomID.Entry_Hall])
Office =            Room(2, "Office", 0, 1, 1, connectionList=[RoomID.Entry_Hall])
Entry_Hall =        Room(3, "Entry Hall", 1, 1, 1, connectionList=[RoomID.Office,RoomID.Garage,RoomID.Kitchen])
Garage =            Room(4, "Garage", 2, 1, 1, connectionList=[RoomID.Entry_Hall])
Kitchen =           Room(5, "Kitchen", 1, 2, 1, connectionList=[RoomID.Entry_Hall,RoomID.Living_Room,RoomID.Basement,RoomID.Landing],roomInventory=[Ethan])
Daughter_Room =     Room(6, "Daughter's Room", 0,3,1,connectionList=[RoomID.Living_Room])
Living_Room =       Room(7, "Living Room",1,3,1, connectionList=[RoomID.Daughter_Room,RoomID.Kitchen,RoomID.Back_Patio,RoomID.Down_Bathroom])
Down_Bathroom =     Room(8, "Downstairs Bathroom",2,3,1, connectionList=[RoomID.Living_Room])
Back_Patio =        Room(9, "Backyard Patio",1,4,1, connectionList=[RoomID.Living_Room,RoomID.Pool])
Pool =              Room(10, "Pool",2,4,1, connectionList=[RoomID.Back_Patio])
Closet =            Room(11, "Walk-in Closet",1,0,2, connectionList=[RoomID.Mast_Bedroom])
Mast_Bathroom =     Room(12, "Master Bathroom",0,1,2, connectionList=[RoomID.Mast_Bedroom])
Mast_Bedroom =      Room(13, "Master Bedroom",1,1,2, connectionList=[RoomID.Mast_Bathroom,RoomID.Closet,RoomID.Landing])
Son_Room =          Room(14, "Son's Room",0,2,2, connectionList=[RoomID.Landing])
Landing =           Room(15, "Upper Landing", 1,2,2, connectionList=[RoomID.Kitchen,RoomID.Mast_Bedroom,RoomID.Son_Room,RoomID.Studio])
Studio =            Room(16, "Art Studio",1,3,2, connectionList=[RoomID.Landing])



roomList = [Basement,
            Front_Yard,
            Office,
            Entry_Hall,
            Garage,
            Kitchen,
            Daughter_Room,
            Living_Room,
            Down_Bathroom,
            Back_Patio,
            Pool,
            Closet,
            Mast_Bathroom,
            Mast_Bedroom,
            Son_Room,
            Landing,
            Studio
            ]

print(Kitchen.GetRoomConnections())
print(Entry_Hall.GetRoomInventory())
print(Kitchen.GetRoomInventory())
EntityMove(Ethan,Entry_Hall)
print(Entry_Hall.GetRoomInventory())
print(f"Ethan is now in {GetEntityRoomName(Ethan)}")
print(random.choice(GetEntityRoom(Ethan).GetRoomConnections()))

#Code in ways for entities to target each other that aren't dependent on entities knowing things about the room. Room is calling entity functions and feeding in parameters. Have director be over rooms. Director calls updates on rooms.
#Any knowledge of character surroundings should come from game world. It shouldn't be stored inside the entity. Also, have a subclass of entity for characters, then inanimate objects.
#Entities should have their own coordinates,but the world should keep track of where they are. In update have characters and items send coordinates to director.