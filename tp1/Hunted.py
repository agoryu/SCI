from Agent import Agent

class Hunted(Agent):

    def __init__(self, x, y):
        Agent.__init__(self, x, y, 0, 0)
        self.color = 'yellow'

    def decide(self, sma):
        env = sma.getEnv()
        coord = self.checkCase(env)

        env.setAgent(coord[0], coord[1], self)
        env.setEmptyCell(self.x, self.y)

        self.x = coord[0]
        self.y = coord[1]

    def isHunter(self):
        return False

    def isHunted(self):
        return True
