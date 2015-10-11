from Agent import Agent

class Hunted(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'yellow'

    def decide(self, sma):
        self.move(sma)

    def isHunter(self):
        return False

    def isHunted(self):
        return True
