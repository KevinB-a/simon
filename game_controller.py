class Game_controller :

    def __init__(self):
        self.round = round
        player = Player()
        self.numbers_list = []

    def reload_game(self):
        """"""
        pass

    def level_difficulty(self):
        """"""
        print("choisir la difficulté facile, moyen ou difficile")
        while not in ["facile", "moyen", "difficile"]:
            self.difficulty=input("choisir la difficulté :")
        return self.difficulty

    def add_player_entry(self):
        """"""
        pass

    def compare_value(self):
        """"""
        pass

    def display_random(self):
        """"""
        pass
