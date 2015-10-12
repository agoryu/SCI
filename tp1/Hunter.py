from Agent import Agent
from random import *
import random

class Hunter(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'green'

        
    def isHunter(self):
        return True


    def decide(self, sma):
        env = sma.getEnv()
        dijsktra = sma.dijsktra
        mini = 1000
        x = self.x
        y = self.y

        for d in dijsktra:
            for i in range(-1,2):
                for j in range(-1,2):
                    if(i==0 and j==0):
                        continue
                    if(sma.isFree(self.x+i, self.y+j)):
                        if(d[self.x+i][self.y+j] < mini):
                            mini = d[self.x+i][self.y+j]
                            x = self.x+i
                            y = self.y+j
            #if(sma.isFree(self.x-1, self.y)):
            #    if(d[self.x-1][self.y] < mini):
            #        mini = d[self.x-1][self.y]
            #        x = self.x-1
            #        y = self.y
            #if(sma.isFree(self.x, self.y+1)):
            #    if(d[self.x][self.y+1] < mini):
            #        mini = d[self.x][self.y+1]
            #        x = self.x
            #        y = self.y+1
            #if(sma.isFree(self.x, self.y-1)):
            #    if(d[self.x][self.y-1] < mini):
            #        mini = d[self.x][self.y-1]
            #        x = self.x
            #        y = self.y-1

        env.setAgent(x, y, self)
        env.setEmptyCell(self.x, self.y)
        self.x = x
        self.y = y

        # Tuer le hunted autour
        hunted = self.huntedAround(sma)
        if(hunted.isHunted()):
            hunted.die(sma)

        
    def huntedAround(self, sma):
        """
        @return agent hunted autour de cet agent hunter s'il y en a
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

                if(cell.isHunted()):
                    return cell

        return cell
