import random


class Sequence :

    def __init__(self):
        """ """
        self.random_list = []
        self.max_random = None

    def add_random(self):
        """add a random number in random list """
        self.number = random.randrange(0,self.max_random) # the value of max_random is given in the
        self.random_list.append(self.number)              # method change_range in the class Game_controller
        return self.random_list
