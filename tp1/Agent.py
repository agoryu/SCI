from Cell import Cell
from random import *
import random

class Agent(Cell):

    def __init__(self, x, y, pasX, pasY):
        """
        Construit un agent simple, pour une bille.
        @param x: position en x
        @param y: position en y
        @param pasX: le déplacement en x
        @param pasY: le déplacement en y
        """
        Cell.__init__(self,x,y)
        
        self.pasX = int(pasX)
        self.pasY = int(pasY)
        self.color = choice(['blue', 'red', 'green', 'magenta'])

    def isAgent(self):
        """
        @return vrai, un Agent est forcément agent
        """
        return True

    
    def decide(self, sma):
        """
        Décide du déplacement de la bille en fonction de 
        l'environnement. 
        @param sma: le modèle qui gère l'environnement et les agents
        """
        env = sma.getEnv()

        nextX = self.x + self.pasX
        nextY = self.y + self.pasY

        if(env.isToric()):
            nextX = nextX % env.getLengthX()
            nextY = nextY % env.getLengthY()
        else:
            if(nextX<0 or nextX>=env.getLengthX()):
                self.pasX *= -1
            if(nextY<0 or nextY>=env.getLengthY()):
                self.pasY *= -1
            nextX = self.x + self.pasX
            nextY = self.y + self.pasY
            
        if(env.isFree(nextX, nextY)):
            # déplacement de la bille sur sa trajectoire  
            env.setAgent(nextX, nextY, self)
            env.setEmptyCell(self.x,self.y)
            self.x = nextX
            self.y = nextY
        else:
            # rebond car autre bille sur la trajectoire
            self.pasX *= -1
            self.pasY *= -1
            
                    
    def getPasX(self):
        return self.pasX

    def getPasY(self):
        return self.pasY

    def checkCase(self, env):
        tabX = list(range(-1, 1))
        tabY = list(range(-1, 1))

        random.shuffle(tabX)
        random.shuffle(tabY)

        for x in tabX:
            for y in tabY:
                posX = self.x+x
                posY = self.y+y
                if(env.isFree(posX, posY)):
                    return (posX, posY)
        return (0,0)

    def die(self, sma):
        sma.removeAgent(self)

    def goTo(self, sma, x, y):
        """
        Force cette agent à aller en x et y même si l'emplacement est non
        vide.
        """       
        env = sma.getEnv()

        if(env.getCell(x,y).isAgent()):
            raise ValueError("Case n'est pas libre.")

        env.setAgent(x, y, self)
        env.setEmptyCell(self.x, self.y)
        self.x = x
        self.y = y
        
