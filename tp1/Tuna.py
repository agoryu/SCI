from Agent import Agent
from random import *
import random

class Tuna(Agent):

    def __init__(self, x, y, pasX, pasY):
        Agent.__init__(self, x, y, pasX, pasY)
        self.PERIOD = 20
        self.age = 1
        self.color = 'blue'

    def isShark(self):
        return False

    def isTuna(self):
        return True


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
    
    def sharkAround(self, env):

        nearX = -1
        nearY = -1

        rx = list(range(-1,1))
        ry = list(range(-1,1))

        random.shuffle(rx)
        random.shuffle(ry)
        
        for i in rx:
            for j in ry:

                if(i==0 and j==0):
                    # Ma position!
                    continue

                if(env.isToric):
                    nearX = (self.x + j) % env.getLengthX()
                    nearY = (self.y + i) % env.getLengthY()
                else:
                    nearX = self.x + j
                    nearY = self.y + i

                    # gestion des bords
                    if(nextX<0 or nextX>=env.getLengthX() or
                       nextY<0 or nextY>=env.getLengthY()):
                        continue

                cell = env.getCell(nearX, nearY)

                if(cell.isShark()):
                    return cell

        return False
    
    def move(self, sma):
        env = sma.getEnv()

        #si il y a un requin on part
        if(self.sharkAround(env)):
            nextX = self.x * -1
            nextY = self.y * -1
        #sinon choix aleatoire
        else:
            nextX = self.x + choice([-1,0,1])
            if(nextX == 0):
                nextY = self.y + choice([-1,1])
            else:
                nextY = self.y + choice([-1,0,1])

        #verification de la disposition du terrain
        if(env.isToric()):
            nextX = nextX % env.getLengthX()
            nextY = nextY % env.getLengthY()
        else:
            if(nextX<0 or nextX>=env.getLengthX() or
                nextY<0 or nextY>=env.getLengthY()):
                case = self.checkCase(env)
                nextX = case[0]
                nextY = case[1]
         
        if(env.isFree(nextX, nextY)):
            # déplacement de la bille sur sa trajectoire  
            env.setAgent(nextX, nextY, self)
            env.setEmptyCell(self.x,self.y)
            self.x = nextX
            self.y = nextY
        else:
            case = self.checkCase(env)
            env.setAgent(case[0], case[1], self)
            env.setEmptyCell(self.x,self.y)
            self.x = case[0]
            self.y = case[1]



