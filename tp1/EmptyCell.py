from Cell import Cell

class EmptyCell(Cell):
    
    def isAgent(self):
        """
        @return faux, une EmptyCell n'est pas un agent.
        """
        return False

    def isTuna(self):
        return False

    def isShark(self):
        return False
