from tkinter import *
from Controler import Controler

class EnvironmentG:

    def __init__(self, fenetre, tailleX, tailleY, tailleCase, sma, nbTours, ralentisseur):
        self.sma = sma
        self.canvas = Canvas(fenetre, width=tailleX*tailleCase, height=tailleY*tailleCase, bg='white')
        self.tailleCase = tailleCase
        self.canvas.pack()
        controler = Controler(sma, self, nbTours, ralentisseur)

        tunaLab = Label(fenetre, text="Thon", fg="blue")
        tunaLab.pack()
        sharkLab = Label(fenetre, text="Requin", fg="red")
        sharkLab.pack()
        
        #bouton de demarrage contenant la methode de lancement de la simu
        boutonStart = Button(fenetre, text="start", command=controler.run)
        boutonStart.pack()

        self.initEnvG()

    def initEnvG(self):
        self.canvas.delete("all")
        for c in self.sma.getListAgent():
            posX = c.x*self.tailleCase
            posY = c.y*self.tailleCase
            idA = self.canvas.create_rectangle(posX, posY, posX+self.tailleCase, posY+self.tailleCase, fill=c.color, outline=c.color)

    def drawEnvG(self):
        self.canvas.delete("all")
        for c in self.sma.getListAgent():
            posX = c.x*self.tailleCase
            posY = c.y*self.tailleCase
            idA = self.canvas.create_rectangle(posX, posY, posX+self.tailleCase, posY+self.tailleCase, fill=c.color, outline=c.color)
        self.canvas.update_idletasks()
