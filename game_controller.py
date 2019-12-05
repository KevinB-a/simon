import os

import time

from player import *

from sequence import *

import random

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
        """method to choose difficulty """
        print("choisir la difficulté facile, moyen ou difficile")
        while self.difficulty not in ["facile", "moyen", "difficile"]:
            self.difficulty=input("choisir la difficulté :")
        return self.difficulty

    def add_player_entry(self):
        """method to add the player number"""
        return int(input("entrez votre nombre :"))
        self.clear()

    def compare_value(self):
        """method to compare numbers_list and random_list"""
        for element in self.sequence.random_list :
            player_choice=self.add_player_entry()
            if element != player_choice :
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

    def change_range(self):

        if self.level_difficulty() =="facile":
            self.number = random.randrange(0,11)

        if self.level_difficulty() == "moyen" :
            self.number = random.randrange(0,21)

        if self.level_difficulty() == "difficile" :
            self.number = random.randrange(0,101)

    def change_time(self):

        if self.level_difficulty() =="facile":
            time.sleep(3)

        if self.level_difficulty() == "moyen" :
            time.sleep(2)

        if self.level_difficulty() == "difficile" :
            time.sleep(1)
