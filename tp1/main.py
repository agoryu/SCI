# On importe Tkinter
from tkinter import *
from SMA import SMA
from EnvironmentG import EnvironmentG
from EmptyCell import EmptyCell

############### recuperation arguments ####################
tailleX = int(sys.argv[1])
tailleY = int(sys.argv[2])
tailleCase = int(sys.argv[3])
ralentisseur = int(sys.argv[4])
nbBille = int(sys.argv[5])
torique = bool(sys.argv[6])

############### initialisation des agents et envvironnement ###################
environnement = []
for i in range(0, tailleX-1):
    environnement.append([])
    for j in range(0, tailleY-1):
        environnement[i].append([EmptyCell(i,j)])
fenetre = Tk()
############### lancement de la simulation ##################
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase)
sma = SMA(environnement, environnementG)

for i in range(0, nbBille):
	x = 0
	y = 0
	while(not sma.isFree(x,y)):
		x = random.randint(0, tailleX)
		y = random.randint(0, tailleY)
	sma.addAgent(Agent(x, y, 0, 0))
sma.run(1000)

# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
