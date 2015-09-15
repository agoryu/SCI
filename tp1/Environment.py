class Environment:

    def __init__(self, rows, cols):
        """
        Initialise l'environnement.
        @param rows: nombre de lignes.
        @param cols: nombre de colonnes.
        """
        try:
            rows = int(rows)
            if rows<0:
                raise ValueError("rows is negative")
        except ValueError:
            rows = 10
            print("Error with rows")
        finally:
            print("rows : " + str(rows))
            
        try:
            cols = int(cols)
            if cols<0:
                raise ValueError("cols is negative")
        except ValueError:
            cols = 10
            print("Error with cols")
        finally:
            print("cols : " + str(cols))
        
        self.rows = rows
        self.cols = cols
        self.grid = []
        
