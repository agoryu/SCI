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
nbTours = 1000

fenetre = Tk()
environnement = Environment(tailleX, tailleY, False)
############### lancement de la simulation ##################
sma = SMA(environnement, True)

for i in range(0, nbHunter + nbHunted + nbWall):
    x = choice(range(tailleX))
    y = choice(range(tailleY))
    while(not sma.isFree(x,y)):
        x=choice(range(tailleX))
        y=choice(range(tailleY))
    
    if(nbHunter > 0):
        sma.addAgent(Hunter(x, y))
        nbHunter -= 1
    elif(nbHunted > 0):
        sma.addAgent(Hunted(x, y))
        nbHunted -= 1
    else:
        sma.addAgent(Wall(x, y))
        nbWall -= 1
                                                                                            
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase, sma, nbTours, ralentisseur)

huntedLab = Label(fenetre, text="Hunted", fg="orange")
huntedLab.pack()
hunterLab = Label(fenetre, text="Hunter", fg="green")
hunterLab.pack()
wallLab = Label(fenetre, text="Wall", fg="#582900")
wallLab.pack()

# On demarre la boucle Tkinter qui s interompt quand on ferme la fenetre
fenetre.mainloop()
