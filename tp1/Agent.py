from Cell import Cell

class Agent(Cell):

    def __init__(self, x, y, pasX, pasY):
        Cell.__init__(self,x,y)
        
        self.pasX = int(pasX)
        self.pasY = int(pasY)
        self.idA = 0

    def isAgent(self):
        """
        @return vrai, un Agent est forcément agent
        """
        return True

    def decide(sma):
        i = 1+1    

    def getId(self):
        return self.idA

    def setId(self, idA):
        self.idA = idA

    def getPasX(self):
        return self.pasX

    def getPasY(self):
        return self.pasY
