from Agent import Agent
from random import *
import random

class Hunted(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'yellow'


    def isHunted(self):
        return True

    
    def decide(self, sma):
        
        env = sma.getEnv()
        hunter = self.hunterAround(sma)

        if(hunter.isHunter()):
            movX = self.x - hunter.getX()
            movY = self.y - hunter.getY()
            next = env.normalizeCoord(self.x+movX, self.y+movY)
            if(sma.isFree(next[0], next[1])):
                self.goTo(sma, next[0], next[1])
                return
            
        self.move(sma)
        


    def hunterAround(self, sma):
        """
        @return agent hunter autour de cet agent hunted s'il y en a
        un. Sinon, retourne case vide.

        """
        env = sma.getEnv()

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

                if(cell.isHunter()):
                    return cell

        return cell
