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
torique = bool(sys.argv[6])


fenetre = Tk()
environnement = Environment(tailleX, tailleY)
############### lancement de la simulation ##################
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase)
sma = SMA(environnement, environnementG)

for i in range(0, nbBille):
    x = 0
    y = 0
    while(not sma.isFree(x,y)):
        x=choice(range(tailleX))
        y=choice(range(tailleY))
    sma.addAgent(Agent(x, y, 0, 0))
sma.run(1000)


# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
