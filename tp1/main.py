# On importe Tkinter
from tkinter import *

#taille fenetre
tailleX = sys.argv[1]
tailleY = sys.argv[2]
tailleCase = sys.argv[3]

ralentisseur = sys.argv[4]
nbBille = sys.argv[5]

torique = sys.argv[6]

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

environnementG=Canvas(fenetre, width=tailleX*tailleCase, height=tailleY*tailleCase, backgroud='white')
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
