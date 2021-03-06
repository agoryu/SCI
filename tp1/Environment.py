from Cell import Cell
from EmptyCell import EmptyCell
from Agent import Agent

class Environment:

    def __init__(self, lengthX, lengthY, toric):
        """
        Initialise l'environnement.
        @param lengthX: nombre de colonnes.
        @param lengthY: nombre de lignes.
        @param toric: booléen indiquant si l'environnement 
        est torique ou non.
        """
        try:
            lengthX = int(lengthX)
            if lengthX<0:
                raise ValueError("lengthX is negative")
        except ValueError:
            lengthX = 10
            print("Error with lengthX")
        finally:
            print("lengthX : " + str(lengthX))
            
        try:
            lengthY = int(lengthY)
            if lengthY<0:
                raise ValueError("lengthY is negative")
        except ValueError:
            lengthY = 10
            print("Error with lengthY")
        finally:
            print("lengthY : " + str(lengthY))

        self.toric = bool(toric)
        
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.grid = []
        
        for x in range(lengthX):
            self.grid.append([])
            for y in range(lengthY):
                self.grid[x].append(EmptyCell(x, y))

    def isToric(self):
        """
        @return: Vrai si environnement torique, Faux sinon.
        """
        return self.toric

    
    def isFree(self, x, y):
        """
        @return: Vrai si la case en x et y est libre, sinon Faux
        """
        x = int(x)
        y = int(y)
        if(x<0 or x>=self.lengthX or y<0 or y>=self.lengthY):
            return False
        return not self.grid[x][y].isAgent()
    

    def getCell(self, x, y):
        """
        @param x: position en x
        @param y: position en y
        @return: la case en x et y de l'environnement
        """
        return self.grid[x][y]


    def setEmptyCell(self, x, y):
        """
        Fixe une nouvelle case vide en x et y.
        @param x: position en x
        @param y: position en y
        """
        self.grid[x][y] = EmptyCell(x,y)


    def setAgent(self, x, y, a):
        """
        Met l'agent a dans la case en x et y.
        @param x: position en x
        @param y: position en y
        @param a: l'agent à mettre dans l'environnement.
        """
        if (not a.isAgent()):
            raise ValueError("a n'est pas agente")
        else:
            self.grid[x][y] = a


    def getGrid(self):
        """
        @return: la grille de l'environnement
        """
        return self.grid

    def normalizeCoord(self, x, y):
        """
        @param x: la coordonnée en x à normaliser
        @param y: la coordonnée en y à normaliser
        @return: les coordonnées correct dans l'environnement 
        qu'il soit torique ou non.
        """
        normX = x
        normY = y
        if(self.isToric()):
            normX = x % self.getLengthX()
            normY = y % self.getLengthY()
        else:
            if(x<0):
                normX = 0
            if(x>=self.getLengthX()):
                normX = self.getLengthX() - 1
            if(y<0):
                normY = 0
            if(y>=self.getLengthY()):
                normY = self.getLengthY() - 1
                
        return (normX, normY)

    def getLengthX(self):
        return self.lengthX

    def getLengthY(self):
        return self.lengthY
