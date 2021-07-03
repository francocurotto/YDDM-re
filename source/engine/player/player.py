from player.crest_pool import CrestPool
from dungobj.monster_lord import MonsterLord
from dungeon.dungeon_tile import DungeonTile

class Player():
    """
    The player that is playing the duel.
    """
    DIM_LIMIT = 12
    def __init__(self, playerid, dicepool):
        self.id = playerid
        self.dicepool = dicepool
        self.crestpool = CrestPool()
        self.dimdice = []
        self.ml = MonsterLord()
        self.monsters = []
        self.items = []
        self.tiles = []

    def create_tile(self, dungobj=None):
        """
        Create player tile with dungeon object in it.
        """
        tile = DungeonTile(dungobj)
        self.tiles.append(tile)
        return tile

    def create_ml_tile(self):
        """
        Create a player tile with the monster lord in it.
        """
        return self.create_tile(self.ml)

    def hit_dim_limit(self):
        """
        True if player hit the dimension limit.
        """
        return len(self.dimdice) >= self.DIM_LIMIT
