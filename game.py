class Game:
    """ Initiates new game """

    def __init__(self, game_type, player_1, player_2):
        self.game_type = game_type
        self.end = False
        self.player_1 = player_1
        self.player_2 = player_2

    def start(self):
        self.player_1.throws()
        self.player_2.throws()