class SMA

    def __init__(self, environnement, agent):
        self.environnement = environnement
        self.agent = agent

    def init_environnement(self):
        for ligne in environnement:
            for case in ligne:
                case = EmptyCell()

    def run(self, nbTours):
        for a in self.agent:
            a.decide()
            #voir pour executer les changement dans la fenetre
