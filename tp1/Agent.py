from Cell import Cell

class Agent(Cell):

    def __init__(self, x, y, pasX, pasY):
        Cell.__init__(self,x,y)
        
        self.pasX = int(pasX)
        self.pasY = int(pasY)
        self.idA = 0

    def isAgent(self):
        """
        @return vrai, un Agent est forcément agent
        """
        return True

    def decide(self, sma):
	#proposition : si la continuation ou le rebond ne marche pas
	#cherche une position libre en iterant sur les tableaux        
	#tabx = [1,1,0,-1,-1,-1,0,1]
        #taby = [0,1,1,1,0,-1,-1,-1]

        disp = str("id: " + repr(self.idA)+ ", pas x:" + repr(self.pasX) + " y:" + repr(self.pasY))
        fichier.write(disp)
        print(disp)
        
        env = sma.getEnv()

        nextX = int(self.x + self.pasX)
        nextY = int(self.y + self.pasY)
        
        if(env.isToric()):
            nextX = int(nextX % env.getLengthX())
            nextY = int(nextY % env.getLengthY())
        else:
            if(nextX<0 or nextX>=env.getLengthX()):
                self.pasX *= -1
            if(nextY<0 or nextY>=env.getLengthY()):
                self.pasY *= -1
            nextX = int(self.x + self.pasX)
            nextY = int(self.y + self.pasY)
                    
        if(env.isFree(nextX, nextY)):
            # déplacement de la bille sur sa trajectoire
            env.setAgent(nextX, nextY, self)
            env.setEmptyCell(self.x,self.y)
            self.x = nextX
            self.y = nextY
        else:
            # rebond car autre bille sur la trajectoire
            self.pasX *= -1
            self.pasY *= -1
            # /!\ peux provoquer boucle infini, si bille entre deux autres
            # on pourrait empêcher cela avec un nouveau param: self.decide(sma, rec+1)
            #self.decide(sma)

            # solution alternative: si rebond, on reverse les pas et on fera le pas au prochain tour
                    
    def getId(self):
        return self.idA

    def setId(self, idA):
        self.idA = idA

    def getPasX(self):
        return self.pasX

    def getPasY(self):
        return self.pasY
