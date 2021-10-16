from dungeon.dungeon import Dungeon

class Duel():
    """
    Contains the state of the game in progress.
    """
    def __init__(self, player1, player2, dungeon):
        self.player1 = player1
        self.player2 = player2
        self.players = [self.player1, self.player2]
        self.dungeon = Dungeon(self.players, dungeon)

    def remove_summon(self, summon):
        """
        Remove summon from player list and dungeon.
        """
        player = self.get_player_summon(summon)
        summon.remove_from_player(player)
        self.dungeon.remove_summon(summon)

    def get_player_summon(self, summon):
        """
        Get the player that posses summon.
        """
        for player in self.players:
            if summon in player.summons:
                return player
