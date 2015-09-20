from tkinter import *
from Controler import Controler

class EnvironmentG:

    def __init__(self, fenetre, tailleX, tailleY, tailleCase, sma, nbTours):
        self.sma = sma
        self.canvas = Canvas(fenetre, width=tailleX, height=tailleY, bg='white')
        self.tailleCase = tailleCase
        self.canvas.pack()
        controler = Controler(sma, self, nbTours)
        boutonStart = Button(fenetre, text="start", command=controler.run)
        boutonStart.pack()
        self.initEnvG()

    def initEnvG(self):
        for c in self.sma.getListAgent():
            posX = c.x*self.tailleCase
            posY = c.y*self.tailleCase
            idA = self.canvas.create_rectangle(posX, posY, posX+self.tailleCase, posY+self.tailleCase, fill='blue')
            c.setId(idA)

    def drawEnvG(self):
        for a in self.sma.getListAgent():
            idA = a.getId()
            self.canvas.move(idA, a.getPasX(), a.getPasY())
