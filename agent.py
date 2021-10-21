from entity import Entity
class Agent(Entity):
    def __init__(self, agentName):
        Entity.__init__(self, agentName)
        self.__agentName = agentName