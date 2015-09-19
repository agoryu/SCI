from tkinter import *

class EnvironmentG:

    def __init__(self, fenetre, tailleX, tailleY, tailleCase):
        self.canvas = Canvas(fenetre, width=tailleX, height=tailleY, bg='white')
        self.tailleCase = tailleCase
        self.canvas.pack()

    def drawEnvG(self, sma):
        for l in self.sma.getEnv():
            for c in l:
                environnementG.create_rectangle(c.x, c.y, c.x+tailleCase, c.y+tailleCase, fill='blue')
