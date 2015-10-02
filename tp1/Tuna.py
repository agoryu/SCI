from Agent import Agent
from random import *
import random

class Tuna(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.PERIOD = 20
        self.age = 1
        self.color = 'blue'

    def isShark(self):
        return False

    def isTuna(self):
        return True


    def reproduction(self, sma):
        case = self.checkCase(sma.getEnv())
        if(case == (self.x, self.y)):
            return False
        else:
            sma.addAgent(Tuna(case[0], case[1]))
            return True

    def decide(self, sma):
        if(self.age%self.PERIOD == 0):
            if(not self.reproduction(sma)):
                self.move(sma)
        else:
            self.move(sma)
        self.age += 1
    
    def sharkAround(self, env):
        """
        @return: un requin autour de cette case, une case 
        vide si il y en a pas.
        """
        nearX = -1
        nearY = -1

        rx = list(range(-1,2))
        ry = list(range(-1,2))

        random.shuffle(rx)
        random.shuffle(ry)
        
        for i in rx:
            for j in ry:

                if(i==0 and j==0):
                    # Ma position!
                    continue

                near = env.normalizeCoord(self.x+i, self.y+j)
                cell = env.getCell(near[0], near[1])

                if(cell.isShark()):
                    return cell

        return cell
    
    
    def move(self, sma):
        env = sma.getEnv()

        #si il y a un requin on part
        shark = self.sharkAround(env)
        if(shark.isShark()):
            movX = self.x - shark.getX()
            movY = self.y - shark.getY()
            next = env.normalizeCoord(self.x+movX, self.y+movY)
        #sinon choix aleatoire
        else:
            next = self.checkCase(env)
            if(next == (self.x, self.y)):
                return
       
        if(env.isFree(next[0], next[1])):
            # déplacement du thon sur le next  
            env.setAgent(next[0], next[1], self)
            env.setEmptyCell(self.x, self.y)
            self.x = next[0]
            self.y = next[1]
        else:
            next = self.checkCase(env)
            if(next == (self.x, self.y)):
                return
