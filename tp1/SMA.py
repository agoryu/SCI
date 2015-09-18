from EmptyCell import EmptyCell

class SMA:

    def __init__(self, environnement, environnementG):
        self.environnement = environnement
        self.environnementG = environnementG
        self.agent = []
        self.nbAgent = 0

    def run(self, nbTours):
        for a in self.agent:
            a.decide()
            #voir pour executer les changement dans la fenetre
            environnementG.drawEnvG(self)

    def addAgent(self, a):
        self.environnement[a.x][a.y] = a
        self.agent.append(a)

    def isFree(self, x, y):
        return not self.environnement[x][y].isAgent()

    def getEnv(self):
        return self.environnement
