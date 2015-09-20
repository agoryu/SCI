from EmptyCell import EmptyCell

class SMA:

    def __init__(self, environnement):
        self.environnement = environnement
        self.agents = []
        self.nbAgent = 0

    def run(self):
        for a in self.agents:
            a.decide(self)

    def addAgent(self, a):
        self.environnement.setAgent(a.x, a.y, a)
        self.agents.append(a)

    def isFree(self, x, y):
        return not self.environnement.getCell(x, y).isAgent()

    def getEnv(self):
        return self.environnement.getGrid()

    def getListAgent(self):
        return self.agents
