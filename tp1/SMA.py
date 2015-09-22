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
        """
        Ajout l'agent a à l'environnement et à la liste 
        d'agents
        @param a: l'agent à ajouter
        """
        self.environnement.setAgent(a.x, a.y, a)
        self.agents.append(a)

    def removeAgent(self, a):
        """
        Supprime l'agent a à l'environnement et à la liste 
        d'agents
        @param a: l'agent à supprimer
        """
        self.environnement.setEmptyCell(a.x, a.y)
        self.agents.remove(a)

    def isFree(self, x, y):
        return not self.environnement.getCell(x, y).isAgent()

    def getEnv(self):
        return self.environnement

    def getListAgent(self):
        return self.agents
