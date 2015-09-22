from Agent import Agent
from random import *

class Tuna(Agent):

    def __init__(self, x, y, pasX, pasY):
        Agent.__init__(self, x, y, pasX, pasY)
        self.PERIOD = 20
        self.age = 1
        self.color = 'blue'

    def isShark(self):
        return False


    def reproduction(self, sma):
        case = self.checkCase(sma.getEnv())
        if(case == (0,0)):
            return False
        else:
            pasX = choice([-1,0,1])
            pasY = choice([-1,0,1])
            sma.addAgent(Tuna(case[0], case[1], pasX, pasY))
            return True

    def decide(self, sma):
        if(self.age%self.PERIOD == 0):
            if(not self.reproduction(sma)):
                self.move(sma)
        else:
            self.move(sma)
        self.age += 1
        
    def move(self, sma):
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


