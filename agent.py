from entity import Entity
class Agent(Entity):
    def __init__(self, agentID, agentName):
        Entity.__init__(self,agentID,agentName)
        self.__agentID = agentID
        self.__agentName = agentName