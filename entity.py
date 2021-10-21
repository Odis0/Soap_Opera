class Entity:
    def __init__(self, entityID, entityName):
        self.__entityID = entityID
        self.__entityName = entityName

    def GetEntityID(self):
        return self.__entityID

    def SetEntityID(self, entityID):
        self.__entityID = entityID


    def GetEntityName(self):
        return self.__entityName