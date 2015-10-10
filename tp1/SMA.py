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

        self.dijsktra = []
    
    def run(self):
        hunted = self.getHunted()
        self.dijsktra = self.createDijsktra(hunted[0])

        for a in self.agents:
            a.decide(self)

    def initDijsktra(self)
        
        dijsktra = []
        sizeX = environnement.getLengthX()
        sizeY = environnement.getLengthY()

        for i in range(0, sizeX):
            self.dijsktra.append([])
            for j in range(0, sizeY):
                self.dijsktra[i].append(-1)

        return dijsktra

    def getHunted(self):
        hunted = []
        for a in self.agent:
            if(a.isHunted()):
                hunted.append(a)
        return hunted

    def createDijsktra(self, a):
        x = a.getX()
        y = a.getY()
        cases = [(x,y,0)]

        dijsktra = self.initDijsktra()

        while(not cases == []):
            current = cases.popleft()
            x = current[0]
            y = current[1]
            cpt = current[2]
            dijsktra[x][y] = cpt
            if(not (x, y, cpt) in cases):
                if(self.isFree(x+1,y) and dijsktra[x+1][y] == -1):
                    cases.append((x+1, y, cpt+1))
                if(self.isFree(x-1,y) and dijsktra[x-1][y] == -1):
                    cases.append((x-1, y, cpt+1))
                if(self.isFree(x,y+1) and dijsktra[x][y+1] == -1):
                    cases.append((x, y+1, cpt+1))
                if(self.isFree(x,y-1) and dijsktra[x][y-1] == -1):
                    cases.append((x, y-1, cpt+1))


    def addAgent(self, a):
        """
        Ajout l'agent a à l'environnement et à la liste 
        d'agents
        @param a: l'agent à ajouter
        """
        cell = self.environnement.getCell(a.getX(),a.getY())
        #if(cell.isAgent()):
        #    errMsg = "Les agents ne peuvent pas se chevaucher"
        #    raise ValueError(errMsg)

        self.nbAgent += 1
        if(a.isShark()):
            self.nbShark += 1
        if(a.isTuna()):
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

        self.nbAgent -= 1
        
        if(a.isTuna()):
            self.nbTuna -= 1
            
        if(a.isShark()):
            self.nbShark -= 1

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
