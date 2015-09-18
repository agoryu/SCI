# On importe Tkinter
from tkinter import *
from SMA import SMA

############### recuperation arguments ####################
tailleX = int(sys.argv[1])
tailleY = int(sys.argv[2])
tailleCase = int(sys.argv[3])
ralentisseur = int(sys.argv[4])
nbBille = int(sys.argv[5])
torique = bool(sys.argv[6])

############### initialisation des agents et envvironnement ###################
agent = [nbBille]
environnement = [tailleX][tailleY]

############### lancement de la simulation ##################
sma = SMA(environnement, agent)
sma.run(1000)

################ partie graphique a voir ###################
# On crée une fenêtre, racine de notre interface
fenetre = Tk()

environnementG=Canvas(fenetre, width=tailleX, height=tailleY, bg='white')
environnementG.pack()
pos = 250
environnementG.create_rectangle(pos, pos, pos+tailleCase, pos+tailleCase, fill='blue')
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
