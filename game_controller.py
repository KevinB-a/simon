import os

import time

from player import *

from sequence import *

class Game_controller :

    def __init__(self):
        self.round = 1
        self.player = Player()
        self.numbers_list = []
        self.sequence = Sequence()
        self.difficulty = None

    def reload_game(self):
        """method to ask the user if he wants to launch an another game"""


    def level_difficulty(self):
        """method to choose difficulty (fonctionnel)"""
        print("choisir la difficulté facile, moyen ou difficile")
        while self.difficulty not in ["facile", "moyen", "difficile"]:
            self.difficulty=input("choisir la difficulté :")
        return self.difficulty

    def add_player_entry(self):
        """method to add the player number (fonctionnel)"""
        self.player_number = int(input("entrez votre nombre :"))
        #self.numbers_list.append(self.player_number)
        self.clear()
        return self.player_number

    def compare_value(self):
        """method to compare numbers_list and random_list"""
        if self.numbers_list == self.sequence.random_list :
            return True
        return False

    def display_random(self):
        """ method to display one by one every random number in the list"""
        self.sequence.add_random()
        for element in self.sequence.random_list:
            print(element)
            time.sleep(3)
            self.clear()

    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')

    def initialize_player(self):
        """method to initialize the name of the player"""
        self.player.enter_name()
