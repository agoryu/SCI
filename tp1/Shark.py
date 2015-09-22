from Agent import Agent

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
        self.age = 0
        self.hunger = 0

    def isShark(self):
        """
        @return Vrai, les agent requin sont des requin
        """
        return True

    def decide(self, sma):
        if(self.hunger > 3):
            self.die()

        tuna = tunaAround()
        if(tuna.isEmpty()):
            move(sma)
        else:
            eat(tuna)
            
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

    def eat(self, tuna):
        tuna.die()
        self.hunger = 0

        
    def die(self, sma):
        sma.removeAgent(self)
