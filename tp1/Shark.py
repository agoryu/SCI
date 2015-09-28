from Agent import Agent
from random import *
import random

class Shark(Agent):

    def __init__(self, x, y, pasX, pasY):
        """
        Allocation d'un agent requin.
        @param x: position en x
        @param y: position en y
        @param pasX: le déplacement en x
        @param pasY: le déplacement en y
        """
        Agent.__init__(self,x,y,pasX,pasY)
        self.color = 'black'
        self.age = 1
        self.hunger = 0


        
    def isShark(self):
        """
        @return Vrai, les agent requin sont des requin
        """
        return True

    def isTuna(self):
        return False
    
    def decide(self, sma):
        #MODIF temps de vie
        if(self.hunger > 7):
            self.die(sma)

        tuna = self.tunaAround(sma)
        if(tuna.isTuna()):
            self.eat(sma, tuna)
        else:
            if(self.age % 10 == 0):
                self.reproduction(sma)
            else:
                self.move(sma)
            self.hunger += 1
        self.age += 1

    
    def reproduction(self, sma):
        case = self.checkCase(sma.getEnv())
        if(case == (0,0)):
            return False
        else:
            pasX = choice([-1,0,1])
            pasY = choice([-1,0,1])
            sma.addAgent(Shark(case[0], case[1], pasX, pasY))
            return True

            
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

    def eat(self, sma, tuna):
        tuna.die(sma)
        self.goTo(sma, tuna.x, tuna.y)
        self.hunger = 0

    def tunaAround(self, sma):
        env = sma.getEnv()

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

                if(cell.isTuna()):
                    return cell

        return cell
                    
                        
                
