from Cell import Cell
from EmptyCell import EmptyCell
from Agent import Agent

class Environment:

    def __init__(self, lengthX, lengthY):
        """
        Initialise l'environnement.
        @param lengthX: nombre de colonnes.
        @param lengthY: nombre de lignes.
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
        
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.grid = []
        
        for x in xrange(lengthX):
            self.grid.append([])
            for y in xrange(lengthY):
                self.grid[x].append(EmptyCell(x, y))


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
