# On importe Tkinter
from tkinter import *
from SMA import SMA
from EnvironmentG import EnvironmentG
from Environment import Environment
from Agent import Agent
from random import *
from Hunter import Hunter
from Hunted import Hunted
from Wall import Wall

############### recuperation arguments ####################
tailleX = int(sys.argv[1])
tailleY = int(sys.argv[2])
tailleCase = int(sys.argv[3])
ralentisseur = int(sys.argv[4])
nbHunter = int(sys.argv[5])
nbHunted = int(sys.argv[6])
nbWall = int(sys.argv[7])

fenetre = Tk()
environnement = Environment(tailleX, tailleY, False)
############### lancement de la simulation ##################
sma = SMA(environnement)

for i in range(0, nbHunter + nbHunted + nbWall):
    x = choice(range(tailleX))
    y = choice(range(tailleY))
    while(not sma.isFree(x,y)):
        x=choice(range(tailleX))
        y=choice(range(tailleY))
    if(nbHunter > 0)
        sma.addAgent(Hunter(x, y))
    else if(nbHunted > 0)
        sma.addAgent(Hunted(x, y))
    else
        sma.addAgent(Wall(x, y))
                                                                                            
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase, sma, nbTours, ralentisseur)

# On demarre la boucle Tkinter qui s interompt quand on ferme la fenetre
fenetre.mainloop()
