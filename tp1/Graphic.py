import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Graphic:

    def __init__(self, title, xlabel, ylabel):
        plt.title(title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(1,1,1)

        self.ani = animation.FuncAnimation(self.fig, animate, interval=1000)
        plt.show()

    def setDataX(self, dataX):
        self.ax1.plot(dataX)
        #self.h.set_ydata(dataY)
