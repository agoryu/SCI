from Agent import Agent

class Hunter(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'green'

    def decide(self, sma):
        return
