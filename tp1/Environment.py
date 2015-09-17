class Environment:

    def __init__(self, lengthX, lengthY):
        """
        Initialise l'environnement.
        @param lengthX: nombre de colonnes.
        @param lengthY: nombre de lignes.
        """
        try:
            lengthX = int(lengthX)
            if lengthX<0:
                raise ValueError("lengthX is negative")
        except ValueError:
            lengthX = 10
            print("Error with lengthX")
        finally:
            print("lengthX : " + str(lengthX))
            
        try:
            lengthY = int(lengthY)
            if lengthY<0:
                raise ValueError("lengthY is negative")
        except ValueError:
            lengthY = 10
            print("Error with lengthY")
        finally:
            print("lengthY : " + str(lengthY))
        
        self.lengthX = lengthX
        self.lengthY = lengthY
        self.grid = []
        
