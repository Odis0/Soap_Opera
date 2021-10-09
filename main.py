
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



class Room:
    def __init__(self, roomName, xAxis, yAxis, zAxis):
        self.__roomName = roomName
        self.__roomCoordinates = (xAxis, yAxis, zAxis)


roomList = [Room("Basement", 1 , 2, 0),
            Room("Front Yard", 0 , 1, 1),
            Room("Office", 0, 1, 1),
            Room("Entry Hall", 1, 1, 1),
            Room("Garage", 2, 1, 1),
            Room("Kitchen", 1, 2, 1),
            Room("Daughter's Room", 0,3,1),
            Room("Living Room",1,3,1),
            Room("Downstairs Bathroom",2,3,1),
            Room("Backyard Patio",1,4,1),
            Room("Pool",2,4,1),
            Room("Walk-in Closet",1,0,2),
            Room("Master Bathroom",0,1,2),
            Room("Master Bedroom",1,1,2),
            Room("Son's Room",0,2,2),
            Room("Upper Landing", 1,2,2),
            Room("Art Studio",1,3,2)
            ]
