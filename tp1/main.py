# On importe Tkinter
from tkinter import *

#taille fenetre
tailleX = int(sys.argv[1])
tailleY = int(sys.argv[2])
tailleCase = int(sys.argv[3])

ralentisseur = int(sys.argv[4])
nbBille = int(sys.argv[5])

torique = bool(sys.argv[6])

# On crée une fenêtre, racine de notre interface
fenetre = Tk()

environnementG=Canvas(fenetre, width=tailleX*tailleCase, height=tailleY*tailleCase, bg='white')
environnementG.pack()
environnementG.create_rectangle(500, 500, 500+tailleCase, 500+tailleCase, fill='blue')
# On démarre la boucle Tkinter qui s'interompt quand on ferme la fenêtre
fenetre.mainloop()
