class Controler:

    def __init__(self, sma, envG, nbTours):
        self.sma = sma
        self.envG = envG
        self.nbTours = nbTours

    def run(self):
        for i in range(self.nbTours):
            self.sma.run()
            self.envG.drawEnvG()
