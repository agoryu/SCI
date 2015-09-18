class Cell:

    def __init__(self, x, y):
        """
        Case générique définit par la position en x et en y.
        @param x: position en x
        @param y: position en y
        """
        self.x = int(x)
        self.y = int(y)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def setX(self, x):
        self.x = int(x)

    def setY(self, y):
        self.y = int(y)

    def isAgent(self):
        """
        @return vrai si la case est un agent, faux sinon.
        """
        pass
        
            
