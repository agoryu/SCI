from EmptyCell import EmptyCell
from Graphic import Graphic
import matplotlib.animation as animation

class SMA:

    def __init__(self, environnement):
        self.environnement = environnement
        self.agents = []
        self.nbAgent = 0

        self.nbTour = 0
        self.nbShark = 0
        self.nbTuna = 0
        self.dataShark = []
        self.dataTuna = []
        """
        self.graphic = Graphic()
        self.graphic.addPlot('evolution marine', 'nb poisson', 'temps')
        self.graphic.addPlot('', '', '')
        """
    def run(self):
        for a in self.agents:
            a.decide(self)

    def addAgent(self, a):
        """
        Ajout l'agent a à l'environnement et à la liste 
        d'agents
        @param a: l'agent à ajouter
        """
        if(a.isShark()):
            self.nbShark += 1
        else:
            self.nbTuna += 1
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

    def updateData(self, nbTour):
        self.dataShark.append(self.nbShark)
        self.dataTuna.append(self.nbTuna)
        self.nbTour = nbTour

    def getFigure(self):
        return self.graphic.getFigure()

    def getData(self):
        return (self.dataShark, self.dataTuna, self.nbTour)
