from Agent import Agent

class Hunter(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'green'

    def decide(self, sma):
        env = sma.getEnv()
        dijsktra = sma.dijsktra
        mini = 1000
        x = self.x
        y = self.y

        if(sma.isFree(self.x+1, self.y)):
            mini = dijsktra[self.x+1][self.y]
            x = self.x+1
            y = self.y
        if(sma.isFree(self.x-1, self.y)):
            if(dijsktra[self.x-1][self.y] < mini):
                mini = dijsktra[self.x-1][self.y]
                x = self.x-1
                y = self.y
        if(sma.isFree(self.x, self.y+1)):
            if(dijsktra[self.x][self.y+1] < mini):
                mini = dijsktra[self.x][self.y+1]
                x = self.x
                y = self.y+1
        if(sma.isFree(self.x, self.y-1)):
            if(dijsktra[self.x][self.y-1] < mini):
                mini = dijsktra[self.x][self.y-1]
                x = self.x
                y = self.y-1

        env.setAgent(x, y, self)
        env.setEmptyCell(self.x, self.y)
        self.x = x
        self.y = y

    def isHunter(self):
        return True
