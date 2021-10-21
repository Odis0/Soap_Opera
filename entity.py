class Entity:
    def __init__(self, entityName):
        self.__entityID = None
        self.__entityName = entityName

    def GetEntityID(self):
        return self.__entityID

    def SetID(self, entityID):
        self.__entityID = entityID


    def GetEntityName(self):
        return self.__entityName