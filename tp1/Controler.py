import time

class Controler:

    def __init__(self, sma, envG, nbTours, ralentisseur):
        self.sma = sma
        self.envG = envG
        self.nbTours = nbTours
        self.ralentisseur = ralentisseur

    def run(self):
        for i in range(self.nbTours):
            self.sma.run()
            self.envG.drawEnvG()
            time.sleep(self.ralentisseur/1000)
