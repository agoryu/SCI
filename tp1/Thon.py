class Thon(Agent):

    def __init__(self, x, y, pasX, pasY)
        Agent.__init__(x, y, pasX, pasY)
        self.PERIOD = 5
        self.age = 0
        self.color = 'blue'

    def isShark(self):
        return False


    def decide(self, sma):
        if(self.age%self.PERIOD == 0):
            if(not reproduction(sma)):
                move(sma)
        else
            move(sma)

    def reproduction(self, sma):
        case = checkCase(sma.getEnv())
        if(case == (0,0)):
            return False
        else:
            sma.addAgent(Thon(case(1), case(2)))
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

        self.age += 1

