from Cell import Cell

class Agent(Cell):

    def __init__(self, x, y, pasX, pasY):
        Cell.__init__(self,x,y)
        
        self.pasX = int(pasX)
        self.pasY = int(pasY)

    def isAgent(self):
        """
        @return vrai, un Agent est forcément agent
        """
        return True

    def decide(sma):
        i = 1+1    
