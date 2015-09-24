import matplotlib.pyplot as plt
import time

class Graphic:

    def __init__(self):

        self.fig = plt.figure()
        self.plotArray = []
        #plt.show()

    def getFigure(self):
        return self.fig

    def setData(self, dataX, dataY, numPlot):
        self.plotArray[numPlot].clear()
        self.plotArray[numPlot].plot(dataX, dataY)

    def addPlot(self, title, xlabel, ylabel):
        ax = self.fig.add_subplot(1,1,1)
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        self.plotArray.append(ax)

    def getGraphic(self):
        return plt
