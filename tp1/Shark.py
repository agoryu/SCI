from Agent import Agent
from random import *
import random

class Shark(Agent):

    def __init__(self, x, y):
        """
        Allocation d'un agent requin.
        @param x: position en x
        @param y: position en y
        @param pasX: le déplacement en x
        @param pasY: le déplacement en y
        """
        Agent.__init__(self,x,y,0,0)
        self.color = 'red'
        self.age = 1
        self.hunger = 0
        self.HUNGER_CYCLE = 5
        self.PERIOD = 10


        
    def isShark(self):
        """
        @return Vrai, les agent requin sont des requin
        """
        return True

    def isTuna(self):
        return False
    
    def decide(self, sma):
        if(self.hunger > self.HUNGER_CYCLE):
            self.die(sma)
        else:
            tuna = self.tunaAround(sma)
            hunger_threshold = int((self.HUNGER_CYCLE/4) * 3)
            if(tuna.isTuna() and self.hunger<hunger_threshold):
                self.eat(sma, tuna)
            else:
                if(self.age % self.PERIOD == 0):
                    self.reproduction(sma)
                else:
                    self.move(sma)
                self.hunger += 1
            self.age += 1

    
    def reproduction(self, sma):
        pas = self.checkCase(sma.getEnv())
        if(pas == (0,0)):
            return False
        else:
            caseX = self.x + pas[0]
            caseY = self.y + pas[1]
            sma.addAgent(Shark(caseX, caseY))
            return True

                         
    def move(self, sma):
        env = sma.getEnv()

        # choix aleatoire

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
                pas = self.checkCase(env)
                nextX = self.x + pas[0]
                nextY = self.y + pas[1]
         
        if(env.isFree(nextX, nextY)):
            # déplacement de la bille sur sa trajectoire  
            env.setAgent(nextX, nextY, self)
            env.setEmptyCell(self.x,self.y)
            self.x = nextX
            self.y = nextY
        else:
            pas = self.checkCase(env)
            nextX = self.x + pas[0]
            nextY = self.y + pas[1]

            #verification de la disposition du terrain
            if(env.isToric()):
                nextX = nextX % env.getLengthX()
                nextY = nextY % env.getLengthY()
            else:
                if(nextX<0 or nextX>=env.getLengthX() or
                   nextY<0 or nextY>=env.getLengthY()):
                    pas = self.checkCase(env)
                    nextX = self.x + pas[0]
                    nextY = self.y + pas[1]
            
            if(sma.isFree(nextX, nextY)):
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
                    
                        
                
