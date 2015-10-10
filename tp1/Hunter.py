from Agent import Agent

class Hunter(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'green'

    def decide(saelf, sma):
        env = sma.getEnv()
        dijsktra = sma.dijsktra
        tab = []

        if(sma.isFree(self.x+1, self.y)):
            tab.append(dijsktra[self.x+1][self.y])
        if(sma.isFree(self.x-1, self.y)):
            tab.append(dijsktra[self.x-1][self.y])
        if(sma.isFree(self.x, self.y+1)):
            tab.append(dijsktra[self.x][self.y+1])
        if(sma.isFree(self.x, self.y-1)):
            tab.append(dijsktra[self.x][self.y-1])

        mini = min(tab)

        for i in tab:
            if(i == min):
                
        return

    def isHunter(self):
        return True

    def isHunted(self):
        return False
