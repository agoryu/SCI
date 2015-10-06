from Agent import Agent

class Wall(Agent):

    def __init__(self, x, y):
        Agent.__init__(self,x,y,0,0)
        # Couleur marron
        self.color = '#582900' 

        
    def decide(self, sma):
        """
        Les murs sont des agents qui ne font aucune action.
        """
        return 
