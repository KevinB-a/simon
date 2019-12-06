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
        while self.difficulty not in ["facile", "moyen", "difficile"]:
            self.difficulty=input("choisir la difficulté :")
        return self.difficulty

    def add_player_entry(self):
        """method to add the player number"""
        self.player_entry=int(input("entrez votre nombre :"))
        self.clear()
        return self.player_entry

    def compare_value(self):
        """method to compare numbers_list and random_list"""
        for element in self.sequence.random_list :
            player_choice=self.add_player_entry()
            if element != player_choice :
                return False

    def display_random(self):
        """ method to display one by one every random number in the list"""
        self.change_range()
        self.sequence.add_random()
        for element in self.sequence.random_list:
            print(element)
            self.change_time()
            self.clear()

    def clear(self):
        """method to clear the terminal"""
        os.system('cls' if os.name =='nt' else 'clear')

    def initialize_player(self):
        """method to initialize the name of the player"""
        self.player.enter_name()

    def change_range(self):
        """method to change the range of the numbers """

        if self.level_difficulty() == "facile" :
            self.sequence.max_random = 11

        if self.level_difficulty() == "moyen" :
            self.sequence.max_random = 21

        if self.level_difficulty() == "difficile" :
            self.sequence.max_random = 101

        return self.sequence.max_random

    def change_time(self):
        """methode to change display time """
        if self.level_difficulty() == "facile":
            time.sleep(3)

        if self.level_difficulty() == "moyen" :
            time.sleep(2)

        if self.level_difficulty() == "difficile" :
            time.sleep(1)
