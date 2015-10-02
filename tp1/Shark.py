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
        self.age = 0
        self.HUNGER_CYCLE = 6
        self.hunger = choice(range(int(self.HUNGER_CYCLE/2.0)))
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
            hunger_threshold = self.HUNGER_CYCLE / 4
            if(tuna.isTuna() and self.hunger<hunger_threshold):
                self.eat(sma, tuna)
                self.age += 1
            else:
                if(self.age > self.PERIOD):
                    self.reproduction(sma)
                    self.age = 0
                else:
                    if(tuna.isTuna()):
                        self.eat(sma, tuna)
                        self.age += 1
                    else:
                        self.move(sma)
                self.hunger += 1
            self.age += 1

    
    def reproduction(self, sma):
        case = self.checkCase(sma.getEnv())
        if(case == (self.x, self.y)):
            return False
        else:
            sma.addAgent(Shark(case[0], case[1]))
            return True

                         
    def move(self, sma):
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


    def eat(self, sma, tuna):
        tuna.die(sma)
        self.goTo(sma, tuna.x, tuna.y)
        self.hunger = 0


    def tunaAround(self, sma):
        env = sma.getEnv()

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

                if(cell.isTuna()):
                    return cell

        return cell
                    
                        
                
