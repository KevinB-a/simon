class Player :
    """this class is used for ask the user his name"""

    def __init__(self):
        """ """
        self.name = None
        self.score = 0

    def enter_name(self):
        """method to ask the user his name  """
        if self.name == None :
            self.name = input("entrez votre nom :")
        return self.name
