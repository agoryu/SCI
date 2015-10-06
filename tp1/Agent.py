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
        """
        Retourne les coordonnées d'une case dans le voisinage 
        8-connexe de cette agent. 
        L'emplacement est recherhché aléatoirement et doit être 
        libre.
        Si il n'y a pas d'emplacement libre 
        @return coordonnées (int, int)
        """
        tabX = list(range(-1, 2))
        tabY = list(range(-1, 2))

        random.shuffle(tabX)
        random.shuffle(tabY)

        for x in tabX:
            for y in tabY:
                case = env.normalizeCoord(self.x+x, self.y+y)
                if(env.isFree(case[0], case[1])):
                    return (case[0], case[1])
                
        return (self.x, self.y)

    def die(self, sma):
        sma.removeAgent(self)

        
    def move(self, sma):
        """
        Retourne les coordonnées d'une case dans le voisinage 
        8-connexe de cette agent. 
        L'emplacement doit être libre, sinon si il n'y a pas 
        d'emplacement libre 
        @return coordonnées (int, int)
        """
        env = sma.getEnv()

        # case aleation 

        next = self.checkCase(env)
        if(next == (self.x, self.y)):
            return
       
        if(env.isFree(next[0], next[1])):
            # déplacement du requin sur le next  
            env.setAgent(next[0], next[1], self)
            env.setEmptyCell(self.x, self.y)
            self.x = next[0]
            self.y = next[1]
        else:
            next = self.checkCase(env)
            if(next == (self.x, self.y)):
                return

            
    def goTo(self, sma, x, y):
        """
        Force cette agent à aller en x et y.
        """       
        env = sma.getEnv()

        if(env.getCell(x,y).isAgent()):
            raise ValueError("Case n'est pas libre.")

        env.setAgent(x, y, self)
        env.setEmptyCell(self.x, self.y)
        self.x = x
        self.y = y


    def isShark(self):
        return False

    def isTuna(self):
        return True
