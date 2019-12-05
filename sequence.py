import random

class Sequence :

    def __init__(self):
        """ """
        self.random_list = []

    def add_random(self):
        """add a random number in random list """
        self.number = random.randrange(0,11)
        self.random_list.append(self.number)
        return self.random_list
