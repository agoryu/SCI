# On importe Tkinter
from tkinter import *
from SMA import SMA
from EnvironmentG import EnvironmentG
from EmptyCell import EmptyCell
from Environment import Environment
from Agent import Agent
from Tuna import Tuna
from Shark import Shark
from random import *
from Graphic import Graphic
import matplotlib.pyplot as plt

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
sma = SMA(environnement)

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
    if(i<3*nbBille/4):
        sma.addAgent(Tuna(x, y, pasX, pasY))
    else:
        sma.addAgent(Shark(x, y, pasX, pasY))
    #sma.addAgent(Tuna(x, y, pasX, pasY))
environnementG = EnvironmentG(fenetre, tailleX, tailleY, tailleCase, sma, nbTours, ralentisseur)

#ani = animation.FuncAnimation(sma.getFigure(), sma.updateGraphic, interval=1000)
# On demarre la boucle Tkinter qui s interompt quand on ferme la fenetre
fenetre.mainloop()

"""
graphic = Graphic()
graphic.addPlot('evolution marine', 'nb poisson', 'temps')
graphic.addPlot('', '', '')
data = sma.getData()
graphic.setData(data[0], range(0, len(data[0])), 0)
graphic.setData(data[1], range(0, len(data[1])), 1)
graphic.getGraphic().show()
"""
data = sma.getData()
size = range(0, len(data[0]))
plt.subplot(211)
plt.plot(size, data[0])
plt.plot(size, data[1])

plt.subplot(212)
#lastData = []
#for i in size:
#    lastData.append(data[1][i] / data[0][i])
plt.plot(data[0], data[1], color='black', linewidth=1.0, linestyle='-')

plt.show()
