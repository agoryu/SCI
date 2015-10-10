# On importe Tkinter
from tkinter import *
from SMA import SMA
from EnvironmentG import EnvironmentG
from EmptyCell import EmptyCell
from Environment import Environment
from Agent import Agent
from random import *

############### recuperation arguments ####################
tailleX = int(sys.argv[1])
tailleY = int(sys.argv[2])
tailleCase = int(sys.argv[3])
ralentisseur = int(sys.argv[4])
nbBille = int(sys.argv[5])
torique = ("True" == str(sys.argv[6]))
nbTours = 1000



fenetre = Tk()
environnement = Environment(tailleX, tailleY, torique)
############### lancement de la simulation ##################
sma = SMA(environnement, False)

for i in range(0, nbBille):
    x = choice(range(tailleX))
    y = choice(range(tailleY))
    pasX = 0
    pasY = 0
    while(not sma.isFree(x,y)):
        x=choice(range(tailleX))
        y=choice(range(tailleY))
    pasX = choice([-1,0,1])
    # on ne veux pas de bille immobille alors:
    if(pasX == 0):
        pasY = choice([-1,1])
    else:
        pasY = choice([-1,0,1])
    sma.addAgent(Agent(x, y, pasX, pasY))
    
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase, sma, nbTours, ralentisseur)

# On demarre la boucle Tkinter qui s interompt quand on ferme la fenetre
fenetre.mainloop()
