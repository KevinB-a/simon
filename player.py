class Player :

    def __init__(self):
        """ """
        self.name = None
        self.score = 0

    def enter_name(self):
        """method to ask the user his name (fonctionnel) """
        self.name = input("entrez votre nom :")
        return self.name

    def play_sequence(self):
        """ """
        pass
