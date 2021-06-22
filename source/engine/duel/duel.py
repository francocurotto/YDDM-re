from dungeon.dungeon import Dungeon

class Duel():
    """
    Contains the state of the game in progress.
    """
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]
        self.dungeon = Dungeon(self.players)
