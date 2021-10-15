
import enum
import random
from Entity import Entity
from Room import Room

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
        self.__worldModule3DArray = [[[None for i in range(5)] for j in range(5)] for k in range(5)]
        self.__roomTuples = [
        ("Basement", 1, 2, 0),
        ("Front_Yard", 0, 1, 1),
        ("Office", 0, 1, 1),
        ("Entry_Hall", 1, 1, 1),
        ("Garage", 2, 1, 1),
        ("Kitchen", 1, 2, 1),
        ("Daughter_Room", 0, 3, 1),
        ("Living_Room", 1, 3, 1),
        ("Down_Bathroom", 2, 3, 1),
        ("Back_Patio", 1, 4, 1),
        ("Pool", 2, 4, 1),
        ("Closet", 1, 0, 2),
        ("Mast_Bathroom", 0, 1, 2),
        ("Mast_Bedroom", 1, 1, 2),
        ("Son_Room", 0, 2, 2),
        ("Landing", 1, 2, 2),
        ("Studio", 1, 3, 2)
                    ]

    def GetRoomNameFromTuple(self, roomTuple):
        return roomTuple[0]

    def GetXAxisFromTuple(self, roomTuple):
        return roomTuple[1]

    def GetYAxisFromTuple(self, roomTuple):
        return roomTuple[2]

    def GetZAxisFromTuple(self, roomTuple):
        return roomTuple[3]

    def AddRoom(self, roomName):
        initializedRoom = Room(roomName)
        return initializedRoom

    def AddWorldModule(self, roomTuple):
        initializedRoom = self.AddRoom(self.GetRoomNameFromTuple(roomTuple))
        worldModule = WorldModule(initializedRoom,self.GetXAxisFromTuple(roomTuple),self.GetYAxisFromTuple(roomTuple),self.GetZAxisFromTuple(roomTuple))
        return worldModule

    def InitializeAllWorldModules(self):
        for i in self.__roomTuples:
            initializedWorldModule = self.AddWorldModule(i)
            self.__worldModule3DArray[initializedWorldModule.GetXAxis()][initializedWorldModule.GetYAxis()][initializedWorldModule.GetZAxis()] = initializedWorldModule

    def GetWorldModule3DArray(self):
        return self.__worldModule3DArray


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



# Static objects should be held by the room, but MOVEABLE objects should be independent. XYZ of player should be linked up with the XYZ of the room by the director. OR have a world object that curates lists and passes it to the director. If two things interact, a higher thing should mediate them.


#World Module Creation Function, Including Rooms



world1 = World()
world1.InitializeAllWorldModules()
print(world1.GetWorldModule3DArray()[2][4][1].GetModuleRoom().GetRoomName())




roomList = [
"Basement",
"Front Yard",
"Office",
"Entry Hall",
"Garage",
"Kitchen",
"Daughter's Room",
"Living Room",
"Downstairs Bathroom",
"Backyard Patio",
"Pool",
"Walk-in Closet",
"Master Bathroom",
"Master Bedroom",
"Son's Room",
"Upper Landing",
"Art Studio"
]





''''
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

'''