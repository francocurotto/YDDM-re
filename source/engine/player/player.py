from player.crest_pool import CrestPool
from dungobj.monster_lord import MonsterLord
from dungeon.dungeon_tile import DungeonTile

class Player():
    """
    The player that is playing the duel.
    """
    def __init__(self, dicepool):
        self.dicepool = dicepool
        self.crestpool = CrestPool()
        self.useddice = []
        self.ml = MonsterLord()
        self.tiles = []

    def create_ml_tile(self):
        """
        Create a player tile with the monster lord in it.
        """
        tile = DungeonTile(self.ml)
        self.tiles.append(tile)
        return tile
