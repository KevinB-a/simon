from os import system

from time import sleep

from player import *
class Game_controller :

    def __init__(self):
        self.round = round
        self.player = Player()
        self.numbers_list = []

    def reload_game(self):
        """"""
        pass

    def level_difficulty(self):
        """fonctionnel"""
        print("choisir la difficulté facile, moyen ou difficile")
        self.difficulty = ""
        while self.difficulty not in ["facile", "moyen", "difficile"]:
            self.difficulty=input("choisir la difficulté :")
        return self.difficulty

    def add_player_entry(self):
        """"""
        self.player_number = int(input("entrez votre nombre :"))
        self.numbers_list.append(self.player_number)
        return self.random_list

    def compare_value(self):
        """"""
        pass

    def display_random(self):
        """"""

    def clear(self):
        """ """
        # for windows
        if name == 'nt':
            _ = system('cls')

        # for mac and linux(here, os.name is 'posix')
        else:
            _ = system('clear')
